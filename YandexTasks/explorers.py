"""
Дан список, в которой хранятся исследователи и топонимы (имена мест) где они бывали. Список имеет следующий формат:

    [
        [<explorer1>, <toponym1>, <toponym2>, ...],
        [<explorer2>, <toponym2>, <toponym3>, ...],
        [<explorer3>, <toponym4>, <toponym1>, ...],
    ]
Надо развернуть этот список, таким образом, чтобы на первом месте оказался топоним, а на остальных исследователи.

Формат ввода
    [
        ["Mallory", "Everest", "Mont Blanc", "Pillar Rock"],
        ["Mawson", "South Pole", "New Hebrides"],
        ["Hillary", "Everest", "South Pole"]
    ]
Формат вывода
    [
        ["Everest", "Hillary", "Mallory"],
        ["South Pole", "Hillary", "Mawson"],
        ["Mont Blanc", "Mallory"],
        ["Pillar Rock", "Mallory"],
        ["New Hebrides", "Mawson"]
    ]
"""

l = [
    ["Mallory", "Everest", "Mont Blanc", "Pillar Rock"],
    ["Mawson", "South Pole", "New Hebrides"],
    ["Hillary", "Everest", "South Pole"]
]

d = {}

for item in l:
    for i in item[1:]:
        d[i] = d.get(i, [])

for key in d.keys():
    for lists in l:
        if key in lists:
            d[key].append(lists[0])

res = [[] for i in range(len(d))]
sorted_d = {k: v for k, v in
            sorted(d.items(), key=lambda item: len(item[1]), reverse=True)}
index = 0
for key, value in sorted_d.items():
    res[index].append(key)
    res[index].extend(sorted(value))
    index += 1
print(res)
