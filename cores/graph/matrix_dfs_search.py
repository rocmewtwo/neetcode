# Matrix Depth-First Search

from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, visit) -> int:
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                    (r, c) in visit or grid[r][c] == 1):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            count = 0
            visit.add((r, c))
            count += dfs(r - 1, c, visit)
            count += dfs(r + 1, c, visit)
            count += dfs(r, c - 1, visit)
            count += dfs(r, c + 1, visit)
            visit.remove((r, c))

            return count

        return dfs(0, 0, visit)
