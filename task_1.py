class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val


# Приклад використання:
root = TreeNode(20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)

max_value = find_max_value(root)
print(f"Найбільше значення у дереві: {max_value}")
