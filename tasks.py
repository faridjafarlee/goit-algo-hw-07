from bst import BinarySearchTree, Node


def find_max(root: Node):
    """Task 1: найбільше значення - BST/AVL."""
    if root is None:
        return None
    cur = root
    while cur.right is not None:
        cur = cur.right
    return cur.value


def find_min(root: Node):
    """Task 2: найменше значення - BST/AVL."""
    if root is None:
        return None
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.value


def sum_values(root: Node):
    """Task 3: сума всіх значень - BST/AVL."""
    if root is None:
        return 0

    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.value
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return total


if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [10, 5, 3, 7, 15, 12, 18]:
        bst.insert(v)

    print("Max:", find_max(bst.root))
    print("Min:", find_min(bst.root))
    print("Sum:", sum_values(bst.root))
