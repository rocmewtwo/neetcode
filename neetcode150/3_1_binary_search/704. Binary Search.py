# 704. Binary Search - Easy
# url: https://leetcode.com/problems/binary-search/

from typing import List


# time complexity: O(logn), space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))  # -1
    print(s.search([5], 5))  # 0
    print(s.search([5], 2))  # -1
