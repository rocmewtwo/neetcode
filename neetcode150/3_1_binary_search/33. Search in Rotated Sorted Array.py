# 33. Search in Rotated Sorted Array - Medium
# url: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


# time complexity: O(logn), space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:  # left is sorted
                if nums[l] <= target < nums[mid]:  # target in left side
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # right is sorted
                if nums[mid] < target <= nums[r]:  # target in right side
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(s.search([1], 0))  # -1
