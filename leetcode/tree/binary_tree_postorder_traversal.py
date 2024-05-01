# 145. Binary Tree Postorder Traversal - Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursive_postorder(root)
        return self.iterative_postorder(root)

    def recursive_postorder(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + dfs(root.right) + [root.val]
        return dfs(root)

    def iterative_postorder(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]  # curr, visited
        res = []
        while stack:
            curr, visit = stack.pop()
            if curr:
                if visit:
                    res.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))
        return res
