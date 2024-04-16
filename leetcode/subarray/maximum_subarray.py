# 53. Maximum Subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            cur_sum = max(cur_sum + n, n)  # take n or prev_sum + n
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        return max_sum
