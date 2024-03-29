# 90. Subsets II

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choose i
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # not choose i
            # skip duplicate
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, subset)

        nums.sort()
        dfs(0, [])
        return res
