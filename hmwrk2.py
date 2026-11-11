import time
import threading
import multiprocessing


def cpu_task(n):
    while n > 0:
        n -= 1


def io_task(seconds):
    time.sleep(seconds)


def run_sequential(task, jobs):
    for job in jobs:
        task(job)


def run_threads(task, jobs):
    threads = []
    for job in jobs:
        t = threading.Thread(target=task, args=(job,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def run_processes(task, jobs):
    processes = []
    for job in jobs:
        p = multiprocessing.Process(target=task, args=(job,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def measure(runner, task, jobs):
    start = time.perf_counter()
    runner(task, jobs)
    return time.perf_counter() - start


def print_row(label, times):
    base = times[0]
    cells = [f"{t:5.2f} წმ ({base / t:4.1f}x)" for t in times]
    print(f"{label:<10} | " + " | ".join(cells))


if __name__ == "__main__":
    cpu_jobs = [10_000_000] * 4
    io_jobs = [1.0] * 4

    runners = [run_sequential, run_threads, run_processes]

    cpu_times = [measure(r, cpu_task, cpu_jobs) for r in runners]
    io_times = [measure(r, io_task, io_jobs) for r in runners]

    print(f"{'':<10} | {'თანმიმდევრულად':<16} | {'thread-ები':<16} | {'პროცესები'}")
    print_row("CPU-bound", cpu_times)
    print_row("I/O-bound", io_times)

#CPU-bound ამოცანა thread ებით არ დაჩქარდა რადგან Python ის GIL ის გამო ერთ დროს მხოლოდ ერთ thread ს შეუძლია Python ის კოდის შესრულება ამიტომ thread ები რიგრიგობით იყენებენ ერთ ბირთვს i/o bound ამოცანა კი დაჩქარდა რადგან time.sleep ის  დროს thread GIL ს ათავისუფლებს და სხვა thread ებიც ერთდროულად ელოდებიან ამიტომ საერთო დრო = ერთი ამოცანის დროს