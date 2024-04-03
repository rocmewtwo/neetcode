# 1091. Shortest Path in Binary Matrix

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        length = 1
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        directions = [(i, j) for i in range(-1, 2)
                      for j in range(-1, 2) if (i, j) != (0, 0)]

        while queue:
            for _ in range(len(queue)):  # snapshot queue, clean queue
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                # 8 directions
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                            (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1
