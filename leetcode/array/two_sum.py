# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    # time: O(n), space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping:
                return [mapping[nums[i]], i]

            mapping[target - nums[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
