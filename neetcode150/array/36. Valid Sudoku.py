# 36. Valid Sudoku - Medium
# url: https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)  # key (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in row_set[r]
                        or board[r][c] in col_set[c]
                        or board[r][c] in box_set[(r // 3, c // 3)]
                        ):
                    return False

                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[(r // 3, c // 3)].add(board[r][c])

        return True
