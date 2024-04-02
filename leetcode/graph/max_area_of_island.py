# 695. Max Area of Island

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        # return area
        def dfs(r, c) -> int:
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    (r, c) in visit or grid[r][c] == 0):
                return 0

            area = 1
            visit.add((r, c))
            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area
