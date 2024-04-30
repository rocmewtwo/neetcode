

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder(root):
    stack = []
    curr: Node = root
    res = []

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


def preorder(root):
    stack = []
    curr: Node = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()


def postorder(root):
    stack = [(root, False)]

    while stack:
        curr, visit = stack.pop()
        if curr:
            if visit:
                print(curr.val)
            else:
                stack.append((curr, True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    '''
        1
       2 3
      4   5
    '''
    print("inorder")
    inorder(root)

    print("preorder")
    preorder(root)

    print("postorder")
    postorder(root)
