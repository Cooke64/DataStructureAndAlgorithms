"""
Структура данных стек и реализация определения корректности скобочной последовательности и обратную польскую нотацию.
"""


class Stack:
    def __init__(self, array: list | None = None):
        self._stack = []
        if array:
            self._clear()
            for i in array:
                self._stack.append(i)

    def _clear(self):
        self._stack.clear()

    def size(self):
        return len(self._stack)

    def is_not_empty(self):
        return self.size() > 0

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_not_empty():
            item = self._stack.pop()
            return item

    def get_stack(self):
        return self._stack


def bracket_sequence(arr):
    res = Stack()
    braces = {')': '(', '}': '{', ']': '['}
    for brace in arr:
        if brace in braces.values():
            res.push(brace)
        elif res:
            item = res.pop()
            if braces[brace] != item:
                return False
    return not res.is_not_empty()


def polish_notation(arr):
    res = Stack()
    for i in arr:
        if isinstance(i, int | float):
            res.push(i)
        elif i in '+-/*':
            y = res.pop()
            x = res.pop()
            res.push(eval(f'{x}{i}{y}'))
    return res.pop()


if __name__ == '__main__':
    assert bracket_sequence('()')
    assert bracket_sequence('')
    assert not bracket_sequence('([}])')
    assert not bracket_sequence('{]')
    assert polish_notation([5, 2, '+']) == 7
    assert polish_notation([2, 7, 5, '*', '+']) == 37

    print(polish_notation([3, 4, '*', 2, '*']))
