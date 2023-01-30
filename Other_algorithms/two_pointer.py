def max_consecutive_elements(input_str):
    """Поиск максимального числа подряд идущих букв"""
    result, cur_letter_idx = 0, 0
    while cur_letter_idx < len(input_str):
        next_letter_idx = cur_letter_idx
        while next_letter_idx < len(input_str) and input_str[
            next_letter_idx] == input_str[cur_letter_idx]:
            next_letter_idx += 1
        result = max(result, next_letter_idx - cur_letter_idx)
        cur_letter_idx = next_letter_idx
    return result


def subarray_sum(non_negative_arr, target):
    """
    Поиск подмассива, сумма которого равна заданной.
    Два указателя, изначально указывают на один элемент. Правый указатель передвигаем до тех пор, пока сумма
    становится равной искомой. если сумма больше, то передвигаем левый указатель, а так же из промежуточной суммы вычитаем
    элемент с индексом [текущий индекс левого - 1]
    Не работает с отрицательными числами в массиве.
    """
    right, current_sum = 0, 0
    for left in range(len_arr := len(non_negative_arr)):
        if left > 0:
            current_sum -= non_negative_arr[left - 1]
        if current_sum == target:
            return True
        while right < len_arr and current_sum < target:
            current_sum += non_negative_arr[right]
            right += 1
    return False
