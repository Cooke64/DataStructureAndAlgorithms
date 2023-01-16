"""
Наибольшая общая подпоследовательность.
A,B - массивы чисел длины M и N соответственно
Вопрос: какая наибольшая подпоследовательность у них общая.
Подпоследовательность - список C содержат только элементы A в которых,
но возможно не все
Fij - длина наибольшее возможной подпоследовательности частей A и В
А[0:i] часть А, содержащая первые i элементов and B[0:j] часть В, содержащая первые j элементов
"""


def lss(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


"""
Наибольшая возрастающая подпоследовательность.
Fi НВП для части A[0:i], которая заканчивается и содержит элемент 
ai = A[i-1]
Fi = [a1,a2,a3 .... ai-1, ai]
"""


def gis(A):
    F = [0] * (len(A))
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1
    return max(F)