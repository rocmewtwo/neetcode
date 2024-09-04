# 42. Trapping Rain Water - Hard
# url: https://leetcode.com/problems/trapping-rain-water/


from typing import List


# water[i] = min(L[i], R[i]) - height[i] -> DP. time: O(n), space: O(n)
# water[i] = min(L, R) - height[i] -> two pointers. time: O(n), space: O(1)
# time: O(n), space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        return self.two_pointers(height)
        # return self.dp(height)

    def two_pointers(self, height: List[int]) -> int:
        left_max, right_max = height[0], height[-1]
        l, r = 0, len(height) - 1
        water = 0

        while l < r:
            if left_max < right_max:  # move left
                l += 1  # can work becase leftmost can't trap water
                left_max = max(left_max, height[l])
                # never negative because line 24. left_max is >= height[l]
                water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water += right_max - height[r]

        return water

    def dp(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        water = 0

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        for i in range(0, len(height)):
            water_i = min(max_left[i], max_right[i]) - height[i]
            water += max(0, water_i)

        return water


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(s.trap([4, 2, 0, 3, 2, 5]))  # 9
print(s.trap([4, 2, 3]))  # 1
print(s.trap([4, 2, 3, 1]))  # 1
