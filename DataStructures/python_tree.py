class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = self.right = None


class Tree:
    def __init__(self, items: list[int] = None):
        self.root = None
        if not self.root and items:
            self.root = Node(items.pop(0))
        [self._add_node(self.root, item) for item in items]

    @staticmethod
    def get_size_of_tree(root: Node) -> int:
        if not root:
            return 0
        return max(Tree.get_size_of_tree(root.right),
                   Tree.get_size_of_tree(root.right)) + 1

    @staticmethod
    def find_item(root: Node, item: int) -> Node | None:
        if root:
            if root.value == item:
                return root
            if item < root.value and root.left:
                return Tree.find_item(root.left, item)
            elif item > root.value and root.right:
                return Tree.find_item(root.right, item)

    def __repr__(self):
        res = []

        def inner(root: Node):
            if root:
                res.append(str(root.value))
                inner(root.left)
                inner(root.right)

        inner(self.root)
        res.append('None')
        return '->'.join(res)

    def _add_node(self, root: Node, value):
        if root:
            if value < root.value:
                if root.left:
                    self._add_node(root.left, value)
                else:
                    root.left = Node(value)
            else:
                if root.right:
                    self._add_node(root.right, value)
                else:
                    root.right = Node(value)

    def add_item(self, value):
        if not self.root:
            self.root = Node(value)
        self._add_node(self.root, value)

    def printer(self):
        def inner(root: Node):
            if root:
                print(root.value, end='->')
                inner(root.left)
                inner(root.right)

        inner(self.root)
        print('None')

    @property
    def max_value(self):
        root = self.root
        while root and root.right:
            root = root.right
        return root.value

    @property
    def min_value(self) -> int:
        root = self.root
        while root and root.left:
            root = root.left
        return root.value

    def is_in_tree(self, value: int) -> bool:
        return bool(self.find_item(self.root, value))

    def is_mirror(self) -> bool:
        """
        Дерево называется анаграммой, если оно симметрично относительно своего центра.
        """
        def check_half(left: Node, right: Node) -> bool:
            if not left and not left:
                return True
            if not left or not right:
                return False
            if left.value == right.value:
                left_part = check_half(left.left, right.right)
                right_part = check_half(left.right, right.left)
                return left_part and right_part

        return check_half(self.root.left, self.root.right)

    def get_size(self) -> int:
        return self.get_size_of_tree(self.root)

    def is_balanced(self) -> bool:
        """
        Дерево считается сбалансированным, если левое и правое
        поддеревья каждой вершины отличаются по высоте не больше, чем на единицу.
        """
        def inner(root: Node) -> bool:
            if not root:
                return True
            left_part = self.get_size_of_tree(root.left)
            right_part = self.get_size_of_tree(root.right)
            difference_between = abs(left_part - right_part) <= 1
            if difference_between and inner(root.left) and inner(root.right):
                return True
            return False

        return inner(self.root)

    def add_before(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        if value < self.root.value:
            self.root, new_node.right = new_node, self.root
        else:
            self.root, new_node.left = new_node, self.root

    def sum_tree(self):
        def inner(root: Node):
            if not root:
                return 0
            if root:
                return root.value + inner(root.right) + inner(root.left)

        return inner(self.root)

    def sum_range(self, low, hight):

        def inner(root: Node):
            if not root:
                return 0

            check_node = low <= root.value <= hight
            result = root.value if check_node else 0
            return inner(root.left) + inner(root.right) + result

        return inner(self.root)


tree = Tree([1, 2, 3])
print(tree.sum_tree())
