# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursive_preorder(root)
        return self.iterative_preorder(root)

    def recursive_preorder(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return []
            return [root.val] + dfs(root.left) + dfs(root.right)
        return dfs(root)

    def iterative_preorder(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:  # left or parent
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return res
