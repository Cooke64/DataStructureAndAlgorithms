def quick_sort(arr):
    if len(arr) < 2:
        return

    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    mid = [i for i in arr if i == pivot]
    quick_sort(left)
    quick_sort(right)
    pos = 0
    for i in left + mid + right:
        arr[pos] = i
        pos += 1


arr = [3, 3, 1, 2, 5, 89, 901]
quick_sort(arr)
print(arr)
