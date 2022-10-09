from typing import List, Optional


class Node:
    def __init__(self, data: int = None):
        self.r: Optional[Node] = None
        self.l: Optional[Node] = None
        self.data = data


class TreeStore:
    def __init__(self, data: Optional[List[int]] = None):
        self.root = None
        if self.root is None:
            value = data.pop(0)
            self.root = Node(value)
        for item in data:
            self.__insert(item, self.root)

    def __insert(self, value, root):
        if value < root.data:
            if root.l:
                self.__insert(value, root.l)
            else:
                root.l = Node(value)
        else:
            if root.r:
                self.__insert(value, root.r)
            else:
                root.r = Node(value)

    def insert_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(value, self.root)

    def print_tree(self):
        if self.root:
            self.__printer(self.root)

    def __printer(self, root):
        if root:
            self.__printer(root.l)
            print(root.data)
            self.__printer(root.r)

    def find(self, val):
        if self.root is not None:
            return self.__find(val, self.root)
        else:
            return None

    def __find(self, val, node):
        if val == node.data:
            return node
        elif val < node.data and node.l:
            return self.__find(val, node.l)
        elif val > node.data and node.r:
            return self.__find(val, node.r)
