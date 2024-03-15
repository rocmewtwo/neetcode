from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # find the kth index

        def quick_select(l, r) -> int:
            pivot = nums[r]
            p = l  # every elements left point are smaller than pivot

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # swap r with p
            nums[r], nums[p] = nums[p], nums[r]

            # select
            if k < p:
                return quick_select(0, p-1)
            elif k > p:
                return quick_select(p+1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums)-1)
