def easy_fibonacci(number):
    first, next = 0, 1
    while first < number:
        print(first, end=' ')
        first, next = next, first + next

