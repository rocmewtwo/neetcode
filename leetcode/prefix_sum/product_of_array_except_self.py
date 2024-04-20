# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List


class Solution:
    # time: O(n), space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res
