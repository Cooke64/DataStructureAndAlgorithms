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


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort_classic(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort_classic(array, low, pi - 1)
        quick_sort_classic(array, pi + 1, high)

arr = [3, 2, 5, 1]
print(quick_sort(arr))
