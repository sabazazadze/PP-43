def constant_time(data):
    """O(1) – ოპერაციების რაოდენობა არ არის დამოკიდებული data-ს ზომაზე"""
    operations = 0
    for i in range(3):
        operations += 1
    return operations


def linear_time(data):
    """O(n) – ოპერაციების რაოდენობა = n"""
    operations = 0
    for item in data:
        operations += 1
    return operations


def quadratic_time(data):
    """O(n²) – ოპერაციების რაოდენობა = n * n"""
    operations = 0
    for a in data:
        for b in data:
            operations += 1
    return operations



for size in (5, 10, 20):
    data = list(range(size))
    print(f"n = {size}")
    print(f"  O(1)  -> {constant_time(data)} ოპერაცია")
    print(f"  O(n)  -> {linear_time(data)} ოპერაცია")
    print(f"  O(n²) -> {quadratic_time(data)} ოპერაცია")
    print()