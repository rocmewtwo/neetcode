# 22. Generate Parentheses - Medium
# url: https://leetcode.com/problems/generate-parentheses/


from typing import List


# time complexity: O(2^n), space complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, s):
            if left == right == n:
                res.append(s)
                return

            # can append left
            if left < n:
                dfs(left + 1, right, s + "(")

            # can append right
            if right < left:
                dfs(left, right + 1, s + ")")

        dfs(0, 0, "")
        return res
