# 42. Trapping Rain Water - Hard
# url: https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    # Time complexity: O(n), Space complexity: O(1)
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]  # never be negative after above line
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]  # never be negative after above line
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))  # 9
