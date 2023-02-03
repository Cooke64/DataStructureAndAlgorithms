"""
N черепах движутся друг за другом. Каждая черепаха говорит, что перед
не а черепах и позади b черепах.
Задача: определить количество черепах, которые врут.
"""


def turtle(n, answers: tuple[int, int]):
    all_turtles = set()
    for a, b in answers:
        if a >= 0  and b >= 0 and a + b == n - 1 and a not in all_turtles:
            all_turtles.add(a)
    return len(all_turtles)
