# 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest

from typing import List, Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            # recursive return left and right child
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                # seperate two forest
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

                # delete the current node by returning None to its parent
                return None
            return node

        root = dfs(root)
        # if the root is not deleted, add it to the forest
        if root:
            forest.append(root)
        return forest
