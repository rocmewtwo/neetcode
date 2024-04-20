# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

from typing import List


class Solution:
    # time: O(n), space: O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)  # O(n)

        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum = total - nums[i] - left_sum
            if right_sum == left_sum:
                return i
        return -1

    # time: O(n), space: O(n)
    def pivotIndex2(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        postfix_sum = [0] * len(nums)

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum[i] = total
        total = 0
        for i in reversed(range(len(nums))):
            total += nums[i]
            postfix_sum[i] = total

        for i in range(len(nums)):
            if prefix_sum[i] == postfix_sum[i]:
                return i
        return -1
