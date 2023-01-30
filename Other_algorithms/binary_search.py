def binary_search(arr, target):
    left_idx, right_idx = 0, len(arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx]:
            return True
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
    return False


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


def left_bin_search(left, right, check, params):
    while left < right:
        middle = (left + right) // 2
        if check(params):
            right = middle
        else:
            left = middle + 1
    return left


def right_bin_search(left, right, check, params):
    while left < right:
        middle = (left + right) // 2
        if check(**params):
            left = middle
        else:
            right = middle - 1
    return left


def search_bin(arr, num, more=False):
    # Выбираем знак. Строгое или не строгое сравнение
    # нестрогое сравнение дает первое вхождение элемента, строгое последнее
    sign = ('>=', '>')[more]
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        # Вычисляем выражение, подставив цифры в строку
        if eval(f'{arr[mid]}{sign}{num}'):
            right = mid
        else:
            left = mid + 1
    return left


def get_res(arr, num):
    left = search_bin(arr, num)
    if arr[left] < num:
        left = len(arr)
    right = search_bin(arr, num, more=True)
    if arr[right] <= num:
        right = len(arr)
    return right - left