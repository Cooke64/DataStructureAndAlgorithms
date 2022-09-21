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
