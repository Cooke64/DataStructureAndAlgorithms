from typing import List, Optional


def two_sum(numbers: List[int], find_num: int):
    """Поиск двух чисел в массиве, сумма которых равна заданному числу.
    Если очередное число, вычтенное из искомого числа имеется в наборе уникальных чисел,
    возвращается очередное число разница чисел искомого числа и очередного числа.
    """
    previous = set()
    for number in numbers:
        if find_num - number in previous:
            return find_num - number, number
        previous.add(number)
    return None


def two_sum_2(numbers: List[int], find_num: int):
    for i in range(len(numbers)):
        mid = find_num - numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j] == mid:
                return numbers[i], numbers[j]
    return None


def two_sum_3(numbers: List[int], find_num: int):
    res = {}
    for i in range(len(numbers)):
        if numbers[i] in res:
            x, y = res[numbers[i]], i
            return numbers[x], numbers[y]
        res[find_num - numbers[i]] = i
    return None


print(two_sum_3([1, 2, 3, 4, 6], 3))
