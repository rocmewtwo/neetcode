from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        return self.detuch_flag_sort(nums)
        # return self.bucket_sort(nums)

    def detuch_flag_sort(self, nums: List[int]) -> None:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                swap(nums, l, m)
                l += 1
                m += 1
            elif nums[m] == 2:  # notice we don't increment m
                swap(nums, m, r)
                r -= 1
            else:
                m += 1

    def bucket_sort(self, nums: List[int]) -> None:
        colors = [0] * 3

        for n in nums:
            colors[n] += 1

        k = 0
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[k] = i
                k += 1
