import random


def quick_sort_inplace(arr):
    if len(arr) < 2:
        return

    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    mid = [i for i in arr if i == pivot]
    quick_sort_inplace(left)
    quick_sort_inplace(right)
    pos = 0
    for i in left + mid + right:
        arr[pos] = i
        pos += 1


def quick_sort(xs):
    if xs:
        pivot = xs[0]
        below = [i for i in xs[1:] if i < pivot]
        above = [i for i in xs[1:] if i >= pivot]
        return quick_sort(below) + [pivot] + quick_sort(above)
    else:
        return xs


def sort_quick(arr):

    left = 0
    right = len(arr) - 1
    if len(arr) < 2:
        return
    m = left
    for i in range(left, right):
        if arr[i] < arr[0]:
            arr[i], arr[m] = arr[m], arr[i]
            m += 1
    sort_quick(arr[left:m])
    sort_quick(arr[m:right])



arr = [4,3,2,1]
sort_quick(arr)
print(arr)
