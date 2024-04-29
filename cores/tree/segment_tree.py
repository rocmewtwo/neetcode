from typing import List, Optional


class Node:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left: Optional[Node] = None  # left child
        self.right: Optional[Node] = None  # right child
        self.L = L  # left index of array
        self.R = R  # right index of array


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)

        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # time: O(logn)
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root: Node, index: int, val: int) -> None:
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    # time: O(logn)
    def query(self, L: int, R: int) -> int:
        return self.query_range(self.root, L, R)

    def query_range(self, root: Node, L: int, R: int):
        if L > root.R or R < root.L:  # query range out boundary
            print(f"{L=} {R=} {root.L=} {root.R=} 0")
            return 0

        # case1: range is bigger and includes the whole array -> return total sum of array
        # case2: range is exactly the total array
        if L <= root.L and R >= root.R:
            print(f"{L=} {R=} {root.L=} {root.R=} {root.sum=}")
            return root.sum

        return self.query_range(root.left, L, R) + self.query_range(root.right, L, R)


if __name__ == "__main__":
    tree = SegmentTree([1, 2, 3, 4, 5])

    # print(tree.query(0, 4))
    # print(tree.query(2, 4))
    print(tree.query(1, 3))
    print(tree.query(-1, 10))  # range covery whole array
