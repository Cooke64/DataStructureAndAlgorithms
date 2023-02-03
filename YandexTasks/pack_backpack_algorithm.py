from typing import NamedTuple
from collections.abc import Sequence


class Item(NamedTuple):
    price: int
    weight: int


items = (Item(0, 3), Item(1, 3))


def back_pack(arr: Sequence[Item], weight: int) -> int:
    len_arr = len(arr)
    res = [[0] * (weight + 1) for _ in range(len_arr)]
    for i in range(len_arr):
        for j in range(1, weight + 1):
            item = arr[i]
            if item.weight > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i-1][j], item.price + res[i][j - item.weight])
    return res[-1][-1]


print(back_pack(items, 4))
