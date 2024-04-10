# 337. House Robber III

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # choose root, without root
        def dfs(root) -> List[int, int]:
            if not root:
                return [0, 0]

            left_root, left_no_root = dfs(root.left)
            right_root, right_no_root = dfs(root.right)
            with_root = root.val + left_no_root + right_no_root
            without_root = max(left_root, left_no_root) + \
                max(right_root, right_no_root)

            return [with_root, without_root]

        return max(dfs(root))

# [3,2,3,null,3,null,1]
# [3,4,5,1,3,null,1]
# [4,1,null,2,null,3]
