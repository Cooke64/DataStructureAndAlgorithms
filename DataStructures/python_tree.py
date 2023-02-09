class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = self.right = None


def get_size_of_tree(root: Node):
    if not root:
        return 0
    return max(get_size_of_tree(root.right), get_size_of_tree(root.right)) + 1


class Tree:
    def __init__(self, items: list[int] = None):
        self.root = None
        if not self.root and items:
            self.root = Node(items.pop(0))
        [self.add_item(item) for item in items]

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

    def add_item(self, value):
        def inner(root: Node, data):
            if data < root.value:
                if root.left:
                    inner(root.left, data)
                else:
                    root.left = Node(data)
            else:
                if root.right:
                    inner(root.right, data)
                else:
                    root.right = Node(data)

        inner(self.root, value)

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
    def min_value(self):
        root = self.root
        while root and root.left:
            root = root.left
        return root.value

    def find_item(self, value: int) -> bool:

        def inner(root, item):
            if root:
                if root.value == item:
                    return root.value
                if item < root.value and root.left:
                    return inner(root.left, item)
                elif item > root.value and root.right:
                    return inner(root.right, item)

        return True if inner(self.root, value) else False

    def is_mirror(self):
        def check_half(left: Node, right: Node):
            if not left or not right:
                return False
            if left.value == right.value:
                left_part = check_half(left.left, right.right)
                right_part = check_half(left.right, right.left)
                return left_part and right_part

        return check_half(self.root.left, self.root.right)

    def get_size(self):
        return get_size_of_tree(self.root)

    def is_balanced(self):
        def inner(root: Node):
            if not root:
                return True
            left_part = get_size_of_tree(root.left)
            right_part = get_size_of_tree(root.right)
            difference_between = abs(left_part - right_part) <= 0
            if difference_between and inner(root.left) and inner(root.right):
                return True
            return False

        return inner(self.root)


tree = Tree([2, 4, 78, 345])
print(tree.get_size())
