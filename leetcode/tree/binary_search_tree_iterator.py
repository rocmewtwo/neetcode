# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        # move left to farthest
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        res = self.stack.pop()
        # move left to farthest
        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack
