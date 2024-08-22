# 1937. Maximum Number of Points with Cost - Medium
# https://leetcode.com/problems/maximum-number-of-points-with-cost/

from typing import List


# time complexity: O(n*m)
# space complexity: O(m)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        dp = points[0][:]

        for r in range(1, ROWS):
            left, right = [0] * COLS, [0] * COLS

            # calc left max
            # left[c-1] is the max from 0 - c-1
            # left[c] is the max from 0 - c
            for c in range(COLS):
                if c == 0:
                    left[c] = dp[c]
                else:
                    left[c] = max(dp[c], left[c-1] - 1)

            # calc right max
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1:
                    right[c] = dp[c]
                else:
                    right[c] = max(dp[c], right[c + 1] - 1)

            # calc dp
            for c in range(COLS):
                dp[c] = points[r][c] + max(left[c], right[c])

        return max(dp)


s = Solution()
print(s.maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]))  # 9
print(s.maxPoints([[1, 5], [2, 3], [4, 2]]))  # 11
print(s.maxPoints([[1, 5], [2, 3], [4, 2], [1, 1]]))  # 12
