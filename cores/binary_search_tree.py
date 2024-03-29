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


def remove(curr: Node, val):
    if not curr:
        return None

    if val > curr.val:
        curr.right = remove(curr.right, val)
    elif val < curr.val:
        curr.left = remove(curr.left, val)
    else:
        # case 1: 0 or 1 child
        # case 2: 2 children
        if not curr.left:
            return curr.right
        elif not curr.right:
            return curr.left
        else:
            # find the min node in right subtree
            # min_node = find_min_node(curr.right)
            min_node = curr.right
            while min_node and min_node.left:
                min_node = min_node.left

            curr.val = min_node.val
            curr.right = remove(curr.right, min_node.val)

    return curr


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
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

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
