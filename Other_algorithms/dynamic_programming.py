dots_array = list[int]


def grasshopper(
        n: int,
        restricted: bool = False,
        allowed: dots_array | None = None
) -> int:
    """
    Количество способов дойти до клетки, если ход или 1, или 2, или 3
    Запрещены клетки для посещения 4 и 7.
    n: количество точек для движения
    restricted: есть ли ограничение на движение
    allowed: разрешенные точки для движения. Значение 1 разрешено, 0 нет по индексу.
    """
    if restricted:
        dots = [0, 1, allowed[2]] + [0] * (n - 3)
        for i in range(3, n + 1):
            if allowed[i]:
                dots[i] = dots[i - 1] + dots[i - 2] + dots[i - 3]
        return dots[n]
    dots = [0, 1] + [0] * n
    for i in range(2, n + 1):
        dots[i] = dots[i - 2] + dots[i - 1]
    return dots[n]


def grasshopper_price(n, dots: dots_array) -> int:
    """
    Минимальная стоимость достижения клетки. ДЛя удобства добавлен нулевой элемент, не имеющий стоимости.
    """
    price_list = [0, dots[1], (dots[1] + dots[2])] + [0] * (n - 2)

    for i in range(3, n + 1):
        price_list[i] = dots[i] + min(price_list[i - 1], price_list[i - 2])
    return price_list[n]

