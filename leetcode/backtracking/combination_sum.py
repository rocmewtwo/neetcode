# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_comb, total):
            if total == target:
                res.append(cur_comb.copy())
                return

            if i == len(candidates) or total > target:
                return

            # choose i
            cur_comb.append(candidates[i])
            dfs(i, cur_comb, total + candidates[i])
            cur_comb.pop()

            # not choose i
            dfs(i + 1, cur_comb, total)

        dfs(0, [], 0)
        return res
