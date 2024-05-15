# 286. Walls and Gates
# Islands and Treasure
# https://neetcode.io/problems/islands-and-treasure


from collections import deque
from typing import List


class Solution:
    # time: O(m * n), space: O(m * n)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        # queue treasures
        queue = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))

        # bfs
        level = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = level

                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and
                            (nr, nc) not in visit and grid[nr][nc] != -1):
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            level += 1

        return grid


s = Solution()
print(s.islandsAndTreasure([
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]))

print(s.islandsAndTreasure([
    [2147483647, -1, 0, 2147483647],
    [-1, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]))
