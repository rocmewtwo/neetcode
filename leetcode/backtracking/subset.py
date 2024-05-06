# 78. Subsets
# https://leetcode.com/problems/subsets/description/

from typing import List


class Solution:
    # time: O(n * 2^n), n is copy operation, every number we have 2 choose
    # space: O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())  # copy O(n)
                return

            # choose i
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()  # back

            # not choose i
            dfs(i + 1)

        dfs(0)
        return res
