from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    queue = deque()
    if root:
        queue.append(root)

    while queue:
        node: Node = queue.popleft()

        print(node.val)
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def bfs_level(root):
    queue = deque()
    if root:
        queue.append(root)

    level = 0
    while queue:
        print(f"{level=}")
        for i in range(len(queue)):  # to track level, we need to clean all nodes in this level
            node: Node = queue.popleft()

            print(node.val)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        level += 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    bfs(root)
    bfs_level(root)
