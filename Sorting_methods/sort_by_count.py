def count_sort(arr):
    """
    in-place сортировка подсчетом. Уместна для значений,
    количество которых ограничено.
    """
    if arr:
        min_value = min(arr)
        max_value = max(arr)
        numbers = max_value - min_value + 1
        temp_array = [0] * numbers
        for index in arr:
            temp_array[index - min_value] += 1
        position = 0
        for value in range(numbers):
            for _ in range(temp_array[value]):
                arr[position] = value + min_value
                position += 1
    else:
        raise ValueError('Пустой список!')
