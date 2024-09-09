# 80. Remove Duplicates from Sorted Array II - Medium
# url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count, at most 2
        # if count > 2 -> move index until find next num
        # return index of last

        l = 0
        count = 0
        for i in range(len(nums)):
            if nums[l - 1] != nums[i]:
                count = 0

            if count < 2:
                nums[l] = nums[i]
                count += 1
                l += 1

        return l
