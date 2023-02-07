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
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b
