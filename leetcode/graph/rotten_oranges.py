# 994. Rotting Oranges

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        visit = set()
        rotten = deque()
        fresh = 0

        # init
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # bfs
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while rotten and fresh > 0:
            for _ in range(len(rotten)):  # snapshot of queue
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] != 1):
                        continue
                    rotten.append((nr, nc))
                    # we can reduce space instead using visit we change input to 2
                    visit.add((nr, nc))
                    fresh -= 1
            minutes += 1
        return minutes if not fresh else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting([[0, 2]]))
print(s.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
