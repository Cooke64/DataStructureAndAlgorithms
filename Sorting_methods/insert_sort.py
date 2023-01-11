def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        temp = i
        while temp > 0 and arr[temp - 1] > arr[temp]:
            arr[temp], arr[temp - 1] = arr[temp - 1], arr[temp]
            temp -= 1
