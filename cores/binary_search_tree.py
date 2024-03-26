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


def remove(root: Node, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # case 1: 0 or 1 child
        # case 2: 2 children
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # find the min node in right subtree
            min_node = find_min_node(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)

    return root


def inorder(root: Node):
    if not root:
        return

    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


def preorder(root: Node):
    if not root:
        return

    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)


def postorder(root: Node):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


def reverse_order(root: Node):
    if not root:
        return

    reverse_order(root.right)
    print(root.val, end=' ')
    reverse_order(root.left)


def inorder_list(root: Node) -> list:
    if not root:
        return []

    return inorder_list(root.left) + [root.val] + inorder_list(root.right)


def find_min_node(root: Node) -> Node:
    curr = root
    while curr and curr.left:
        curr = curr.left

    return curr


if __name__ == "__main__":
    root = Node(50)

    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print(inorder_list(root))
    min_node = find_min_node(root)
    print(min_node.val)

    remove(root, 50)
    print(inorder_list(root))

    inorder(root)
    print()

    preorder(root)
    print()

    postorder(root)
    print()

    reverse_order(root)
    print()
