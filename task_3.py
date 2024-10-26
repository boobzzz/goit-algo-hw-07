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


def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)


root = TreeNode(20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)

sum_value = sum_of_values(root)
print(f"Найбільше значення у дереві: {sum_value}")
