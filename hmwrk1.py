import time
import threading


def make_tea(name, seconds):
    print(f"{name}: იწყება")
    time.sleep(seconds)
    print(f"{name}: მზადაა")

teas = [("მწვანე ჩაი", 1.0), ("შავი ჩაი", 1.5), ("ბალახის ჩაი", 2.0)]

start = time.perf_counter()
for name, seconds in teas:
    make_tea(name, seconds)
sequential_time = time.perf_counter() - start
print(f"თანმიმდევრულად: {sequential_time:.1f} წმ")

start = time.perf_counter()
threads = []
for name, seconds in teas:
    t = threading.Thread(target=make_tea, args=(name, seconds))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
threaded_time = time.perf_counter() - start
print(f"thread-ებით: {threaded_time:.1f} წმ")

print(f"დაჩქარება: {sequential_time / threaded_time:.1f}x")
