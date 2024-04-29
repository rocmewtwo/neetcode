# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description/

from typing import List


class Node:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R


class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], L: int, R: int):
        if L == R:
            return Node(nums[L], L, R)

        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        return self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val) -> None:
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def sumRange(self, left: int, right: int) -> int:
        return self.query_range(self.root, left, right)

    def query_range(self, root, left, right) -> int:
        # out boundary
        if left > root.R or right < root.L:
            return 0

        # range covers whole array
        if left <= root.L and right >= root.R:
            return root.sum

        return self.query_range(root.left, left, right) + self.query_range(root.right, left, right)
