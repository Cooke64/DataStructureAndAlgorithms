"""

"""


def f(arr):
    c = 0
    arr = list(set(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[j] - arr[i]) % 200 == 0 and i < j:
                c += 1
    return c


if __name__ == '__main__':
    print(f([100]))
