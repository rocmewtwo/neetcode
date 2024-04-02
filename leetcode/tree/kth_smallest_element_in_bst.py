# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.recursive_kth_smallest(root, k)
        return self.iterative_kth_smallest(root, k)

    def recursive_kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.res

    def iterative_kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while root or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
