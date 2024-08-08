# 885. Spiral Matrix III
# url: https://leetcode.com/problems/spiral-matrix-iii/
# Difficulty: Medium

from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # right -> down -> left -> up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []  # [(r1, c1), ...]
        step = 1
        cur_dir = 0

        while len(res) < rows * cols:  # stop at len(res) == rows * cols
            for _ in range(2):  # every 2 directions, we increment unit
                # walk step
                for _ in range(step):
                    # only add inbound points
                    if (rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols):
                        res.append([rStart, cStart])

                    rStart += directions[cur_dir][0]
                    cStart += directions[cur_dir][1]

                cur_dir = (cur_dir + 1) % 4
            step += 1

        return res


s = Solution()
print(s.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0))
print(s.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4))
