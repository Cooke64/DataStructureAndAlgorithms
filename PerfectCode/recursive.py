def is_power(n):
    """Является ли число степенью двойки."""
    if n % 2 != 0:
        return n == 1
    return is_power(n // 2)


def recursive_sum(a, b):
    """Рекурсивное сложение чисел в диапазоне от start до end."""
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)


def bee(n):
    if n >= -5 and n > 0:
        print(n)
        bee(n - 5)
    print(n)


def get_all_str(data):
    if isinstance(data, str):
        print(data, end=' ')
    if isinstance(data, list | tuple):
        for i in data:
            get_all_str(i)


def get_data_from_dict(data, key):
    if key in data:
        return data[key]

    for _, v in data.items():
        if isinstance(v, dict):
            value = get_data_from_dict(v, key)
            if value:
                return value


def dict_travel(data, path=''):
    for k, v in sorted(data.items()):
        if isinstance(v, dict):
            dict_travel(data[k], path + f'{k}.')
        if type(v) != dict:
            print(f'{path}{k}: {data[k]}')
