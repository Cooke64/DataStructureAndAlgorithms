def merge(arr_1, arr_2):
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
