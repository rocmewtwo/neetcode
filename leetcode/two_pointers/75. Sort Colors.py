# 75. Sort Colors - medium
# url: https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.two_pointers(nums)
        # self.bucket_sort(nums)

    # time: O(n), space: O(1)
    def two_pointers(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1  # don't want to increment i
            i += 1

    # time: O(n), space: O(1)
    def bucket_sort(self, nums: List[int]) -> None:
        bucket = [0, 0, 0]

        for n in nums:
            bucket[n] += 1

        l = 0
        for i in range(3):
            for _ in range(bucket[i]):
                nums[l] = i
                l += 1


s = Solution()
nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)
print(nums)

nums = [2, 0, 1]
s.sortColors(nums)
print(nums)
