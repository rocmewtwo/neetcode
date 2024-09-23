# 11. Container With Most Water - Medium
# url: https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(s.maxArea([1, 1]))  # 1
print(s.maxArea([4, 3, 2, 1, 4]))  # 16
