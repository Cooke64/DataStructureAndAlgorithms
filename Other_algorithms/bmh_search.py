class BMH:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self._len_pattern = len(pattern) - 1
        self._len_text = len(text)
        self._offset = self.get_offset()

    def get_offset(self):
        d = {}
        last_char = ''
        for i, v in enumerate(reversed(self.pattern)):
            if i == 0:
                last_char = v
                continue
            d[v] = d.get(v, i)
        d[last_char] = d.get(last_char, self._len_pattern)
        d['*'] = self._len_pattern
        return d

    def search(self):
        i = j = self._len_pattern
        while i < self._len_text:
            if self.text[i] == self.pattern[j]:
                if j == 0:
                    return i
                j -= 1
                i -= 1
            else:
                i += self._offset.get(self.text[i], self._offset['*'])
                j = self._len_pattern
        return -1


if __name__ == '__main__':
    bmh = BMH('мои давнные', 'данные')
    assert bmh.search() == -1
