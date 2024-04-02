# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursive_inorder(root)
        return self.iterative_inorder(root)

    def recursive_inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.recursive_inorder(root.left) + [root.val] + self.recursive_inorder(root.right)

    def iterative_inorder(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

        return res
