# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List


class Solution:
    # time: O(m + n), space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return self.merge_1loop(nums1, m, nums2, n)
        # return self.merge_2loop(nums1, m, nums2, n)

    def merge_1loop(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        p1, p2 = m - 1, n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1

    def merge_2loop(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        p1, p2 = m - 1, n - 1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else:
                nums1[last] = nums1[p1]
                p1 -= 1
            last -= 1

        while p2 >= 0:
            nums1[last] = nums2[p2]
            last -= 1
            p2 -= 1


s = Solution()
test_cases = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
    ([2, 0], 1, [1], 1)
]

for nums1, m, nums2, n in test_cases:
    s.merge(nums1, m, nums2, n)
    print(nums1)
