# 153. Find Minimum in Rotated Sorted Array - Medium
# url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


from typing import List


# the minimum value will be in the unsorted part
# so we can use binary search to find the unsorted part
# if mid > right -> left side is sorted -> search right side
# else -> right side is sorted -> search left side
# time complexity: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))  # 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(s.findMin([11, 13, 15, 17]))  # 11
