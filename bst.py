class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right