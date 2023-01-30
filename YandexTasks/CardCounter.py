""""
На стол в ряд выложены карточки, на каждой карточке
написано натуральное число. За один ход разрешается взять карточку либо с левого,
либо с правого конца ряда. Всего можно сделать
k ходов. Итоговый счет равен сумме чисел на выбранных карточках. Определите, какой
максимальный счет можно получить по итогам игры.
"""


def card_counter(arr, k):
    if len(arr) == k:
        return sum(arr)
    rang = len(arr) // 2
    left = arr[:rang]
    right = list(reversed(arr[rang:]))
    c = 0
    for _ in range(k):
        min_arr = left if sum(left) >= sum(
            right) and len(left) > 0 else right
        c += min_arr.pop(0)
    return c


if __name__ == '__main__':
    assert card_counter([1, 2, 3, 4, 5], 5) == 15
    assert card_counter([0, 0, 0], 1) == 0
    assert card_counter([150], 1) == 150
