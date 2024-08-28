# 1905. Count Sub Islands - Medium
# url: https://leetcode.com/problems/count-sub-islands/

from typing import List


class Solution:
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            # skip
            if (r == ROWS or r < 0 or c == COLS or c < 0 or grid2[r][c] == 0 or (r, c) in visited):
                return True

            visited.add((r, c))
            res = True

            # false case
            if grid1[r][c] == 0:
                res = False

            # make sure put res in the end
            # run dfs on all 4 directions first
            # if res is False, it will not check the rest
            # we can't concatenate four dfs calls in one line, because we need to run all four dfs calls
            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res

            return res

        ROWS, COLS = len(grid1), len(grid1[0])
        visited = set()
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1

        return count


s = Solution()
grid1 = [[1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1]]

grid2 = [[1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0]]
print(s.countSubIslands(grid1, grid2))  # 3

grid1 = [[1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 0, 1, 0, 1]]

grid2 = [[0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1]]
print(s.countSubIslands(grid1, grid2))  # 2
