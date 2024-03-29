# 39. Combination Sum
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i == len(candidates) or total > target:
                return

            # not choose i
            dfs(i + 1, subset, total)

            # choose i
            subset.append(candidates[i])
            dfs(i, subset, total + candidates[i])
            subset.pop()

        dfs(0, [], 0)
        return res
