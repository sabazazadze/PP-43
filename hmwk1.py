def countdown(start):
    n = start
    while n >= 1:
        yield n
        n -= 1
    yield "სტარტი! 🚀"


def squares_up_to(limit):
    n = 1
    while n * n <= limit:
        yield n * n
        n += 1




launch = countdown(3)
print(next(launch))
print(next(launch))
print(list(launch))
print(list(launch))

print(list(squares_up_to(50)))
print(list(squares_up_to(100)))
for square in squares_up_to(20):
    print(square, end=" ")
print()