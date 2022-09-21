def find_start(arr, target):
    """Нахождение первого вхождения числа. Для поиска find_first_and_last"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_end(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def find_first_and_last_bin(arr, target):
    return find_start(arr, target), find_end(arr, target)