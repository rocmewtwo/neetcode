from typing import List


class Solution:
    # time O(m * n), space O(m * n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = (dp[r - 1][c] if r - 1 >= 0 else 0) + \
                        (dp[r][c - 1] if c - 1 >= 0 else 0)

        return dp[ROWS-1][COLS-1]

    # time O(m * n), space O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * COLS
        dp[COLS-1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < COLS:
                    dp[c] = dp[c] + dp[c + 1]
                    # dp[c] = dp[c] + (dp[c + 1] if c + 1 < COLS else 0)

        return dp[0][0]
