from collections import Counter


def one_world_anangramm(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


def one_world_anangramm_v2(word_1, word_2):
    return word_1 == word_2[::-1]


def is_palindrome(word_1, word_2):
    def get_dict(word):
        hash_dict = {}
        for i in word:
            hash_dict[i] = hash_dict.get(i, 0) + 1
        return hash_dict

    if len(word_1) < len(word_2):
        return False

    hash_1 = get_dict(word_1)
    hash_2 = get_dict(word_2)

    for key in hash_1:
        if key not in hash_2 or hash_1[key] != hash_2[key]:
            return False
    return True


def is_anagram_v2(word_1, word_2):
    return Counter(word_1) == Counter(word_2)
