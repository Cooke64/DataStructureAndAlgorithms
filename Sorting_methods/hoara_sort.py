def quick_sort(arr):
    if len(arr) < 2:
        return

    pivot = arr[0]
    left = [i for i in arr if arr < pivot]
    right = [i for i in arr if arr > pivot]
    mid = [i for i in arr if arr == pivot]
    quick_sort(left)
    quick_sort(right)
    pos = 0
    for i in left + mid + right:
        arr[pos] = i
        pos += 1


arr = [3, 3, 1, 2]
quick_sort(arr)
print(arr)
