# 1448. Count Good Nodes in Binary Tree
# url: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time complexity: O(n), space complexity: O(h)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, max_value):
            nonlocal result
            if not node:
                return

            if node.val >= max_value:
                result += 1

            max_value = max(node.val, max_value)
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, root.val)
        return result


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3, TreeNode(1, TreeNode(3)),
                    TreeNode(4, TreeNode(1), TreeNode(5)))
    print(s.goodNodes(root))  # 4

    root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    print(s.goodNodes(root))  # 3

    root = TreeNode(1)
    print(s.goodNodes(root))  # 1

    root = TreeNode(2, TreeNode(4), TreeNode(3))
    print(s.goodNodes(root))  # 3
