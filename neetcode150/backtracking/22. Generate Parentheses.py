# 22. Generate Parentheses - Medium
# https://leetcode.com/problems/generate-parentheses/


from typing import List


class Solution:
    # time complexity: O(2^n), space complexity: O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open if open < n
        # only add close if close < open
        # valid if open == close == n
        def dfs(open, close):
            if open == close == n:
                res.append(''.join(s))
                return

            if open < n:
                s.append('(')
                dfs(open + 1, close)
                s.pop()

            if close < open:
                s.append(')')
                dfs(open, close + 1)
                s.pop()

        res = []
        s = []
        dfs(0, 0)
        return res
