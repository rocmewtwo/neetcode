# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, cur_comb):
            if i == len(digits):
                res.append("".join(cur_comb))
                return

            for c in mapping[digits[i]]:
                dfs(i + 1, cur_comb + c)

        if digits:
            dfs(0, "")
        return res
