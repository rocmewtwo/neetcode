# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/

from typing import List


# time: O(n * s), memory: O(s)
# n is the len of number, s is the total sum of nums
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(total)

        if total % 2:
            return False

        dp = set()
        dp.add(0)
        target = total // 2

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                next_dp.add(t + nums[i])  # plus
                next_dp.add(t)  # add origins
            dp = next_dp
        return False
