# 1219. Path with Maximum Gold
# https://leetcode.com/problems/path-with-maximum-gold/description/

from typing import List


class Solution:
    # time: O(m * n * 4 ^(m * n)), decision tree: 4 branch, max height of tree (m*n)
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                    (r, c) in visited or grid[r][c] == 0):
                return 0

            visited.add((r, c))
            # 4 directions
            max_gold = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                max_gold = max(max_gold, grid[r][c] + dfs(nr, nc))
            visited.remove((r, c))
            return max_gold

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res
