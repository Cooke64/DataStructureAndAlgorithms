def easy_fibonacci(number):
    first, next_item = 0, 1
    while first < number:
        print(first, end=' ')
        first, next_item = next_item, first + next_item


def fibonacci(n):
    fib_dict = {0: 0, 1: 1}
    if n in fib_dict:
        return fib_dict[n]
    return fibonacci(n - 1) + fibonacci(n - 2)


def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
