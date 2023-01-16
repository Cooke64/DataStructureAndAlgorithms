def is_in_list(num, arr):
    return num in arr


def gcd(num: int, m: int = -1, prefix=None):
    prefix = prefix or []
    m = num if m == -1 else m
    if m == 0:
        print(prefix)
        return

    for i in range(1, num + 1):
        if is_in_list(i, prefix):
            continue
        prefix.append(i)
        gcd(num, m - 1, prefix)
        prefix.pop()


def simple_gcd(num, prefix=''):
    if num == 0:
        print(prefix)
        return
    for i in range(num):
        simple_gcd(num - 1, prefix + '0')
        simple_gcd(num - 1, prefix + '1')


