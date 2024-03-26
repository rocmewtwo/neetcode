class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def insert(root: Node, val):
    if not root:
        return Node(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


def inorrder(root: Node):
    if root:
        inorrder(root.left)
        print(root.val, end=' ')
        inorrder(root.right)


if __name__ == "__main__":
    root = Node(50)

    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    inorrder(root)
