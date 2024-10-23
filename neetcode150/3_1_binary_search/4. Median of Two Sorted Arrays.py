# 4. Median of Two Sorted Arrays - Hard
# url: https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


# the median is the middle value in an ordered integer list. might m1 or (m1 + m2) / 2
# m1 or m2 is always greater than or equal to left side, and less than or equal to right side
# our goal is find the correct partition of A, so that A_left <= B_right and B_left <= A_right
# time complexity: O(log(min(m, n))), space complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # make sure A is shorter than B, so we can do binary search on shorter list
        if len(A) > len(B):
            A, B = B, A

        # search the correct partition of A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            # half - (i + 1) - 1. i + 1 is the length of left side, -1 convert to index
            j = half - i - 2

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if i + 1 < len(A) else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if j + 1 < len(B) else float('inf')

            # find the correct partition
            if A_left <= B_right and B_left <= A_right:
                # even case
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                # odd case
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:  # left side is too big
                r = i - 1
            else:  # right side is too big
                l = i + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
