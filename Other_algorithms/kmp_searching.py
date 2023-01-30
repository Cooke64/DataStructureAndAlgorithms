def kmp(stack, needl):
    index = -1
    for i in range(len(stack) - len(needl) + 1):
        s = True
        for j in range(len(needl)):
            if needl[j] != stack[i + j]:
                s = False
                break
        if s:
            index = i
            break
    return index


def kmp_2(stack, needl):
    for i in range(len(stack) - len(needl) + 1):
        if stack[i: (len(needl) + i)] == needl:
            return i
    return -1


class Kmp:
    def __init__(self, stack, pattern):
        self.stack = stack
        self.pattern = pattern
        self._len_pattern = len(pattern)

    def _find_prefix(self) -> list[int]:
        """
        алгоритм поиска префикса в строке. Возвращает массив, в котором
        значением(числом) является количество подряд совпадающих элементов
        в суффиксе и префиксе
        res[0] = 0, j = 0, i = 0
        если res[j] == res[i], то res[i] == j + 1, i++, j++
        иначе
            если j == 0, то res[i] == 0, i++
            иначе j = res[i-1]
        Сложность O(M)
        лиллил
        [0,0,1,1,2,3]
        """
        res = [0]
        for i in range(1, self._len_pattern):
            j = res[i - 1]
            while j > 0 and self.pattern[i] != self.pattern[j]:
                j = res[j - 1]
            if self.pattern[j] == self.pattern[i]:
                j += 1
            res.append(j)
        return res


    def search_kmp(self):
        """
        Поиск подстроки в строке. Возвращает индексы нахождения начала и конца.
        i == 0, j == 0
        если stack[i] == pattern[j]:
            то i++, j++
            если j == len(pattern)
                Нашли
        иначе пока j > 0 и stack[i] != pattern[j]:
            j = prefix[j - 1]
        """
        prefix = self._find_prefix()
        j = 0
        res = []
        for i in range(len(self.stack)):
            while j > 0 and self.stack[i] != self.pattern[j]:
                j = prefix[j - 1]
                res.clear()
            if self.stack[i] == self.pattern[j]:
                j += 1
                res.append(i)
                if j == self._len_pattern:
                    return res
        return -1



k = Kmp('ароррара', 'ара')



print(k._find_prefix())
