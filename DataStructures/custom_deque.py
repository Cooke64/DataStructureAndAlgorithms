class DequeOverFlow(Exception):
    pass


class EmptyDeque(Exception):
    pass


class CustomDeque:
    def __init__(self, number):
        self.__deque = [None] * number
        self.__max_size = number
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __is_not_empty(self):
        return self.__size != 0

    def __is_overflow(self):
        return self.__size != self.__max_size

    def __change_params(self, item, plus=True):
        return (item + 1 if plus else item - 1) % self.__max_size

    def push_back(self, value):
        if not self.__is_overflow():
            return DequeOverFlow('error')
        self.__deque[self.__tail] = value
        self.__tail = self.__change_params(item=self.__tail)
        self.__size += 1

    def push_front(self, value):
        if not self.__is_overflow():
            return DequeOverFlow('error')
        self.__deque[self.__head - 1] = value
        self.__head = self.__change_params(plus=False, item=self.__head)
        self.__size += 1

    def pop_back(self):
        if not self.__is_not_empty():
            return EmptyDeque('error')
        value = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__tail = self.__change_params(plus=False, item=self.__tail)
        self.__size -= 1
        return value

    def pop_front(self):
        if not self.__is_not_empty():
            return EmptyDeque('error')
        value = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = self.__change_params(item=self.__head)
        self.__size -= 1
        return value


def get_data():
    index = int(input())
    max_size = int(input())
    return index, max_size


def main():
    number_of_command, max_size = get_data()
    q = CustomDeque(max_size)
    for _ in range(number_of_command):
        command, *value = input().split()
        result = getattr(q, command)(*value)
        if result:
            print(result)


if __name__ == '__main__':
    main()
