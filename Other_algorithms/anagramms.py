from collections import Counter


def one_world_anangramm(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


def one_world_anangramm_v2(word_1, word_2):
    return word_1 == word_2[::-1]


def is_anagram(word_1, word_2):
    if len(word_1) < len(word_2):
        return False
    hash_1 = {}
    hash_2 = {}
    for i in word_1:
        hash_1[i] = hash_1.get(i, 0) + 1
    for i in word_2:
        hash_2[i] = hash_2.get(i, 0) + 1
    for key in hash_1:
        if key not in hash_2 or hash_1[key] != hash_2[key]:
            return False
    return True


def is_anagram_v2(word_1, word_2):
    return Counter(word_1) == Counter(word_2)
