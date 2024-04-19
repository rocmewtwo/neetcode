# 42. Trapping Rain Water

from typing import List


class Solution:
    # time: O(n), space: O(1)
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[0], height[r]
        res = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res

    # time: O(n), space: O(n)
    def trap2(self, height: List[int]) -> int:
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        res = 0

        for i in range(1, len(height)):
            max_left[i] = max(height[i - 1], max_left[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])
            res += max(0, min(max_left[i], max_right[i]) - height[i])
        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
print(s.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap2([4, 2, 0, 3, 2, 5]))
