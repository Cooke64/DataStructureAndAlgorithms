def easy_fibonacci(number):
    first, next_item = 0, 1
    while first < number:
        print(first, end=' ')
        first, next_item = next_item, first + next_item


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a