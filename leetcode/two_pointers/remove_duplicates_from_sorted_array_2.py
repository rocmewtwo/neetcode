# 80. Remove Duplicates from Sorted Array II

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        count = 1
        for r in range(1, len(nums)):
            if nums[l-1] != nums[r]:
                count = 0  # reset
            count += 1
            if count <= 2:
                nums[l] = nums[r]
                l += 1
        return l
