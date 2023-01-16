def merge_two_lists(arr_1, arr_2):
    index_1 = index_2 = 0
    result = []
    while index_2 < len(arr_2) and index_1 < len(arr_1):
        if arr_1[index_1] < arr_2[index_2]:
            result.append(arr_1[index_1])
            index_1 += 1
        else:
            result.append(arr_2[index_2])
            index_2 += 1
    return result + arr_1[index_1:] + arr_2[index_2:]


def merge_sort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left = [arr[i] for i in range(mid)]
    right = [arr[i] for i in range(mid, len(arr))]
    merge_sort(left)
    merge_sort(right)
    temp = merge_two_lists(left, right)
    for i in range(len(arr)):
        arr[i] = temp[i]
