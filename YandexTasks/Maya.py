from PerfectCode.timer import timer


def make_dict(s):
    res_dict = {}
    for i in s:
        res_dict[i] = res_dict.get(i, 0) + 1
    return res_dict


def match_dict(dict_1, dict_2):
    matches = 0
    for item in dict_1:
        if item in dict_2 and dict_1[item] == dict_2[item]:
            matches += 1
    return matches


def modify_dict(dict_w, dict_s, symbol, counter):
    ans = 0
    if symbol not in dict_s:
        dict_s[symbol] = 0
    if symbol in dict_w and dict_s[symbol] == dict_w[symbol]:
        ans = -1
    dict_s[symbol] += counter
    if symbol in dict_w and dict_s[symbol] == dict_w[symbol]:
        ans = 1
    return ans


@timer
def get_maya_string(word, string):
    len_word = len(word)
    len_string = len(string)
    dict_1 = make_dict(word)
    dict_2 = make_dict(string[:len_word])
    matching = match_dict(dict_1, dict_2)
    occurrences = 1 if matching == len_word else 0
    for i in range(len_word, len_string):
        matching += modify_dict(dict_1, dict_2, string[i - len_word], -1)
        matching += modify_dict(dict_1, dict_2, string[i], 1)
        if matching == len(dict_1):
            occurrences += 1
    return occurrences


@timer
def get_maya_string_2(word, string):
    len_word = len(word)
    s_w = sorted(word)
    len_string = len(string)
    c = 0
    index = 0
    while index < len_string - len_word:
        if (sorted(string[index: len_word + index])) == s_w:
            c += 1
            index += len_word
        else:
            index += 1
    if sorted(string[index:]) == s_w:
        c += 1
    return c


word = 'ашам'
string = 'маша'*100004
print(get_maya_string_2(word, string))
print('working another')
print(get_maya_string(word, string))