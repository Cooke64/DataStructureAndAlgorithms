def f(s: str):
    len_s = len(s)
    left = right = res = [0] * len_s

    for i in range(len_s - 1):
        if s[i] == s[i+1]:
            continue
        if s[i].lower() == s[i + 1].lower():
            left[i] = 1

    for i in range((len_s - 1), 0, -1):
        if s[i] == s[i-1]:
            continue
        if s[i].lower() == s[i - 1].lower():
            right[i] = 1

    for i in range(len_s):
        res[i] = max(left[i], right[i])

    total = []
    for i in range(len_s):
        if not res[i]:
            total.append(s[i])

    return ''.join(total)


def func(s):
    new_s = f(s)
    if new_s == s or not new_s:
        return new_s
    else:
        return func(new_s)


if __name__ == '__main__':
    assert func('vxOoOoVvx') == 'vxx'
    assert func('abBa') == 'aa'
    assert func('AbBa') == ''
    assert func('a') == 'a'
    assert func('FF') == 'FF'
    assert func('фА') == 'фА'
