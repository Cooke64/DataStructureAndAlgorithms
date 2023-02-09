from typing import List, Union


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes: List[int]):
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
        for i in self:
            result.append(i.value)
        result.append('None')
        return '->'.join([str(i) for i in result])

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def count_list(self) -> int:
        return len([i for i in self])

    def get_by_index(self, index: int, services: bool = False) -> Union[
        Node, str]:
        try:
            position = 0
            node = self.head
            while position != index:
                position += 1
                node = node.next
            return node if services else node.value
        except AttributeError as e:
            raise AttributeError(f'There`s no attribute like {e}')

    def add_before(self, item: str) -> None:
        new_node = Node(item, next=self.head)
        self.head = new_node

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
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_by_index(index, services=True)
        before_node = self.get_by_index(index - 1, services=True)
        before_node.next = node.next

    def reverse_list(self):
        current = self.head
        new_head = None
        while current:
            nxt = current.next
            current.next = new_head
            new_head = current
            current = nxt
        self.head = new_head

    def remove_one_duplicate(self):
        head = self.head
        cur = head
        while cur:
            while cur.next and cur.next.value == cur.value:
                cur.next = cur.next.next
            cur = cur.next
        return head

    def delete_all_duplicates(self):
        head = self.head
        pre = Node(next=head)

        while head and head.next:
            if head.value == head.next.value:
                while head and head.next and head.value == head.next.value:
                    head = head.next
                head = pre.next = head.next
            else:
                pre = pre.next
                head = head.next

        return pre.next

    def removeElements(self, val):
        res = Node(next=self.head)
        current = res
        while current.next:
            if current.next.value == val:
                current.next = current.next.next
            else:
                current = current.next
        return res.next

    def reverse_recursive(self):

        def inner(head):
            if not head:
                return None
            new_head = head
            if head.next:
                new_head = inner(head.next)
                head.next.next = head
            head.next = None

            return new_head

        self.head = inner(self.head)


l = LinkedList([1, 2, 2, 4, 4, 4, 5])
l.reverse_recursive()
print(l)


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
