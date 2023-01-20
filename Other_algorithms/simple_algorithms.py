from typing import List, Optional


def moving_average_method(array: List[int], num: int) -> List[float]:
    """
    Cоздаёт новый массив данных,
    и в нём значение каждой точки высчитывается как среднее
    арифметическое предыдущих num значений из исходного набора.
    """
    result = []
    for i in range(len(array) - 2):
        result.append(sum(array[i:i + num]) / num)
    return result


def searching_substring_in_string(string: str, substring: str) -> int:
    """
    Поиск первого вхождения подстроки в строку через цикл,
    где срез равняется длине подстроки.
    """
    if not string or not substring:
        return -1
    substring_lenght = len(substring)
    for index in range(len(string)):
        if string[index:index + substring_lenght] == substring:
            return index
        return index


def get_excessive_letter(shorter: str, longer: str) -> str:
    """Поиск добавленной лишней буквы в строке. Создает новую строку, где убирается очередная буква из цикла.
    Возвращает строку, где остаются лишние символы.
    """
    for character in shorter:
        longer = longer.replace(character, '', 1)
    return longer


def print_two_array(a: List[int], b: List[int]) -> print:
    """
    Упаковываем два массива функцией zip и итерируемся по элементам.
    Распаковываем кортеж в print поэлементно, вывод через пробел.
    """
    [print(*item, end=' ') for item in zip(a, b)]
    pass


def max_consecutive_elements(arr):
    """
    Моиск максимального элемента в строке.
    """
    total = current_res = 0
    current = arr[0]
    for i in range(1, len(arr)):
        letter = arr[i]
        if letter == current:
            current_res += 1
        else:
            total = max(total, current_res)
            current_res = 1
            current = arr[i]
    return max(total, current_res)


def two_sum(numbers: List[int], find_num: int) -> Optional[int, int]:
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


def is_prime(n):
    """Проверять числа, которые больше чем корень n необязательно. Если у числа nn есть делитель, больший корня из n
    то существует и делитель, меньший корень из n
    """
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def eratosthenes(n):
    """Поиск простых чисел в массиве способом 'Решето Эратосфена' """
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        for j in range(num * num, n + 1, num):
            numbers[j] = False
    return numbers


def fact(x):
    if x < 0:
        return 'Отрицательные числа не считает'
    if x == 0:
        return 1
    return fact(x - 1) * x


def gcd(a, b):
    """Алгоритм Евклида медленный."""
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_2(a, b):
    """Алгоритм Евклида быстрый."""
    return a if b == 0 else gcd(b, a % b)


def custom_pow(a, b):
    """Медленное рекуррентное возведение в степень"""
    return 1 if b == 0 else custom_pow(a, b - 1) * a


def custom_pow_2(a, b):
    """Быстрое рекуррентное возведение в степень"""
    if b == 0:
        return 1
    elif b % 2 == 1:  # Четное значение
        return custom_pow_2(a, b - 1) * a
    else:  # Нечетное значение
        return custom_pow(a ** 2, b // 2)
