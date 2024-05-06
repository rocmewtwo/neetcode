# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/description/

from typing import List


class Solution:
    # time: O(nlogn + n * 2^n) = O(n * 2^n)
    # space: O(n * 2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()  # O(nlogn)

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())  # O(n)
                return

            # choose i
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # not choose i, and skip duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
