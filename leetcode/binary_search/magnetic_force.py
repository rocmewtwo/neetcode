# 1552. Magnetic Force Between Two Balls
# https://leetcode.com/problems/magnetic-force-between-two-balls/description

from typing import List


class Solution:
    def can_place_balls(self, diff_dist, position, m) -> bool:
        pre_pos = position[0]
        placed = 1

        for i in range(1, len(position)):
            # can place ball at ith position
            if position[i] - pre_pos >= diff_dist:
                placed += 1
                pre_pos = position[i]

            if placed == m:
                return True
        return False

    # time: O(nlogMax(position))
    def maxDistance(self, position: List[int], m: int) -> int:
        l, r = 0, max(position)
        res = 0

        position.sort()
        while l <= r:
            mid = l + (r - l) // 2
            if self.can_place_balls(mid, position, m):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res


s = Solution()
print(s.maxDistance(position=[1, 2, 3, 4, 7], m=3))  # 3
print(s.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))  # 999999999
