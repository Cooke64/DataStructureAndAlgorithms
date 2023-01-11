def sort_select_1(data):
    for i, value in enumerate(data):
        minimal = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[minimal] = data[minimal], value
    return data


def sort_select_2(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

