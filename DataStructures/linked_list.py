from typing import List, Union


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes: List[str]):
        """
        Получает первый элемент, который присваивается в self.head, далее через цикл проходит
        все элементы списка поочередно меняя значение node и node.next
        :param nodes: принимает список, элементами которого являются строки.
        """
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(value=item)
                node = node.next

    def __repr__(self):
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next
        result.append('None')
        return '->'.join([str(i) for i in result])

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def count_list(self) -> int:
        counter = 0
        while self.head:
            self.head = self.head.next
            counter += 1
        return counter

    def get_by_index(self, index: int, services: bool = False) -> Union[
        Node, str]:
        try:
            position = 0
            node = self.head
            while position != index:
                position += 1
                node = node.next
            return node if services else node.value
        except:
            raise AttributeError(f'There`s no attribute like {index}')

    def add_before(self, item: str) -> None:
        node = Node(item)
        node.next = self.head
        self.head = node

    def add_after(self, item: str) -> None:
        node = Node(item)
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def insert_by_index(self, index: int, value: str) -> None:
        new_node = Node(value)
        if index == 0:
            self.add_before(value)
            return
        previous_node = self.get_by_index(index - 1, services=True)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def remove_by_index(self, index: int) -> None:
        """

        Если нулевой элемент, то меняется значение головы на следующее значение голловы предыдущего
        Если не нулевой элемент, то меняется местами связка предыдущего элемента и следующего элемента удаялемого
        :param index: Принимает значение индекса, удаляемого объекта.
        :return:
        """
        if index == 0:
            self.head = self.head.next
        node = self.get_by_index(index, services=True)
        before_node = self.get_by_index(index - 1, services=True)
        before_node.next = node.next

    def reverse_list(self):
        current = self.head
        new_head = None
        while current:
            current.next, current, new_head = new_head, current.next, current
        return new_head


def merge_two_list(l1, l2):
    head = cur = Node(0)
    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return head.next


class NodeTest:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def remove_by_index(node, idx):
    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node

    if idx == 0:
        node = node.next_item
    else:
        previous_node = get_node_by_index(node, idx - 1)
        next_node = get_node_by_index(node, idx + 1)
        previous_node.next_item = next_node
    return node
