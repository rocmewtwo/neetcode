# 40. Combination Sum II

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset[:])
                return

            if i == len(candidates) or total > target:
                return

            # choose i
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()

            # not choose i
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, subset, total)

        candidates.sort()
        dfs(0, [], 0)
        return res
