def pascal_triangle(num):
    res = [[1], [1, 1]] + [[] for _ in range(num + 1)]
    for i in range(2, num + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(res[i - 1][j - 1] + res[i - 1][j])
        new_row.append(1)
        res[i] = new_row

    for row in res:
        for num in row:
            print(num, end=' ')
        print()

pascal_triangle(5)
