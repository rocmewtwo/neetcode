# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/description/

from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        return self.dijkstra(grid)
        # return self.dijkstra2(grid)

    # Dijkstra, time: O(ElogE) -> O(ElogV^2) -> O(ElogV)
    # V: n^2 nodes, E: 4 * n^2
    # time: O(n * n * log n)
    def dijkstra(self, grid: List[List[int]]) -> int:
        total_time = 0
        heap = [(grid[0][0], 0, 0)]  # t, r, c
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        while heap:
            t, r, c = heappop(heap)
            if (r, c) in visited:
                continue

            total_time = max(t, total_time)
            if r == ROWS - 1 and c == COLS - 1:
                return total_time

            visited.add((r, c))
            # add four directions
            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (r + rd >= 0 and r + rd < ROWS and
                    c + cd >= 0 and c + cd < COLS and
                        (r + rd, c + cd) not in visited):
                    heappush(heap, (grid[r + rd][c + cd], r + rd, c + cd))

    def dijkstra_visit(self, grid: List[List[int]]) -> int:
        total_time = 0
        heap = [(grid[0][0], 0, 0)]  # t, r, c
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        # if we add start at visit, we can comment 22-23, and add 34
        visited.add((r, c))

        while heap:
            t, r, c = heappop(heap)
            # if (r, c) in visited:
            #     continue

            total_time = max(t, total_time)
            if r == ROWS - 1 and c == COLS - 1:
                return total_time

            # add four directions
            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (r + rd >= 0 and r + rd < ROWS and
                    c + cd >= 0 and c + cd < COLS and
                        (r + rd, c + cd) not in visited):
                    visited.add((r + rd, c + cd))
                    heappush(heap, (grid[r + rd][c + cd], r + rd, c + cd))

    # record max t
    def dijkstra2(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]  # t, r, c
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        while heap:
            t, r, c = heappop(heap)
            if (r, c) in visited:
                continue

            if r == ROWS - 1 and c == COLS - 1:
                return t

            visited.add((r, c))
            # add four directions
            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (r + rd >= 0 and r + rd < ROWS and
                    c + cd >= 0 and c + cd < COLS and
                        (r + rd, c + cd) not in visited):
                    heappush(
                        heap, (max(t, grid[r + rd][c + cd]), r + rd, c + cd))
