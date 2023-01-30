def range_some_query(nums, left, right):
    """Реализация суммы чисел на отрезке через префиксные суммы.
    Создается массив на 1 элемент которого больше исходного. Заполняется суммой
    предыдущего элемента исходного массива и нового массива. Отсчет идет с единицы."""
    result = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        result[i] = result[i - 1] + nums[i - 1]
    return result[right] - result[left]


def find_first_and_last(arr, num):
    """Получаем первый элемент, равный заданному, далее циклом прибавляем к стартовому индексу
    на каждой итерации пока индекс не будет равен длинно массива или перестанет
    быть равным искомому значению.
    """
    length = len(arr)
    for i in range(length):
        if arr[i] == num:
            start = i
            while i + 1 < length and arr[i + 1] == num:
                i += 1
            return start, i
    return -1, -1


def bracket_sequence(arr):
    res = []
    braces = {')': '(', '}': '{', ']': '['}
    for brace in arr:
        if brace in braces.values():
            res.append(brace)
        elif res and braces[brace] == res[-1]:
            res.pop()
        else:
            return False
    return res


def rle(arr):
    total = []
    current = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[current]:
            total.append(f'{i - current}{arr[current]}')
            current = i
    total.append(f'{len(arr) - current}{arr[current]}')
    return ''.join(total)


def max_consecutive_elements(input_str):
    """Поиск максимального числа подряд идущих букв"""
    result, cur_letter_idx = 0, 0
    while cur_letter_idx < len(input_str):
        next_letter_idx = cur_letter_idx
        while next_letter_idx < len(input_str) and input_str[next_letter_idx] == input_str[cur_letter_idx]:
            next_letter_idx += 1
        result = max(result, next_letter_idx - cur_letter_idx)
        cur_letter_idx = next_letter_idx
    return result
