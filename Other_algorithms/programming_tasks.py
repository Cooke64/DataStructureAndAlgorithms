def range_some_query(nums, left, right):
    """Реализация суммы чисел на отрезке через префиксные суммы.
    Создается массив на 1 элемент которого больше исходного. Заполняется суммой
    предыдущего элемента исходного массива и нового массива. Отсчет идет с единицы."""
    result = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        result[i] = result[i - 1] + nums[i - 1]
    return result[right] - result[left]


def find_first_and_last(arr, num):
    """Получаем первый элемент, равный заданному, далее циклом прибавляем к стартовому индексу
    на каждой итерации пока индекс не будет равен длинно массива или перестанет
    быть равным искомому значению.
    """
    lenght = len(arr)
    for i in range(lenght):
        if arr[i] == num:
            start = i
            while i + 1 < lenght and arr[i + 1] == num:
                i += 1
            return start, i
    return -1, -1


def bracket_sequence(arr):
    res = []
    bracket = {')': '(', '}': '{', ']': '['}
    for i in arr:
        if i in bracket.values():
            res.append(i)
        elif res and bracket[i] == res[-1]:
            res.pop()
        else:
            return False
    return res == []

"abcabcbb"
res = 3
start = 4

def lengthOfLongestSubstring(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        # when char already in dictionary
        if ch in dic:
            # check length from start of string to index
            res = max(res, i - start)
            # update start of string index to the next index
            start = max(start, dic[ch] + 1)
        # add/update char to/of dictionary
        dic[ch] = i
    # answer is either in the begining/middle OR some mid to the end of string
    return max(res, len(s) - start)
