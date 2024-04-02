# Matrix Breadth-First Search
# Find shortest path

from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 0

        while queue:
            for i in range(len(queue)):  # snapshoot of queue
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    if (dr + r < 0 or dr + r == ROWS or dc + c < 0 or dc + c == COLS
                            or (dr + r, dc + c) in visit or grid[dr + r][dc + c] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    # add visit to prevent node added to queue twice
                    visit.add((r + dr, c + dc))
            length += 1
        return -1
