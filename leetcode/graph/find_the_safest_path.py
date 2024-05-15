# 2812. Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/description

from heapq import heappop, heappush
from typing import List
from collections import deque


class Solution:
    # bfs go through all 1's cell
    # record the m distance
    # start from 0, 0, greedy choose the max val of distances
    # time: BFS O(n^2) + Dijastra O(n^2 * logn))
    # space: O(n^2)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # start or end are theif
        if grid[0][0] or grid[-1][-1]:
            return 0

        N = len(grid)

        def bfs_compute_distances():
            distances = [[0 for c in range(N)] for r in range(N)]

            # find 1 and compute min distance
            # if bfs every cell O(n^4)
            # but bfs from every thief only takes O(n^2)
            queue = deque()
            visited = set()
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        visited.add((r, c))

            # bfs mark m distance to distances
            level = 0
            while queue:
                for _ in range(len(queue)):  # snapshot and clean stack
                    r2, c2 = queue.popleft()
                    distances[r2][c2] = level

                    # visit 4 directions
                    for nr, nc in [(r2 + 1, c2), (r2 - 1, c2), (r2, c2 + 1), (r2, c2 - 1)]:
                        if (nr >= 0 and nr < N and nc >= 0 and nc < N and (nr, nc) not in visited):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                level += 1
            return distances

        distances = bfs_compute_distances()
        # greedy find greater distance using Dijkstra
        max_heap = [(-distances[0][0], 0, 0)]
        visited = set()
        while max_heap:
            dist, r, c = heappop(max_heap)
            dist = -dist

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r == N - 1 and c == N - 1):
                return dist

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr >= 0 and nr < N and nc >= 0 and nc < N and (nr, nc) not in visited):
                    # record the min distance of path
                    nd = min(dist, distances[nr][nc])
                    heappush(max_heap, (-nd, nr, nc))


s = Solution()
print(s.maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(s.maximumSafenessFactor(
    grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
print(s.maximumSafenessFactor(grid=[[0, 1, 1], [0, 1, 1], [1, 1, 1]]))
