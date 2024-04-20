# 304. Range Sum Query 2D - Immutable

from typing import List


class NumMatrix:
    # time: O(n^2), space: O(n^2)
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # self.prefix = [[0 for j in range(COLS + 1)]
        #                for i in range(ROWS + 1)]
        # fill extra 0 row and col to prevent edge case if
        self.prefix = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                above = self.prefix[r][c + 1]
                self.prefix[r + 1][c + 1] = total + above

    # time: O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_top = self.prefix[row1][col1]
        left_bottom = self.prefix[row2 + 1][col1]
        right_top = self.prefix[row1][col2 + 1]
        right_bottoom = self.prefix[row2 + 1][col2 + 1]
        # print(f"{right_bottoom=} {left_bottom=} {right_top=} {left_top=}")
        return right_bottoom - left_bottom - right_top + left_top


class NumMatrix2:
    # time: O(n^2), space: O(n^2)
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0 for c in range(COLS)] for r in range(ROWS)]
        # caculate prefix sum for every rows
        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                self.prefix[r][c] = total

    # time: O(rows)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        # query range sum from row1 to row2
        for r in range(row1, row2 + 1):
            pre_left = self.prefix[r][col1 - 1] if col1 > 0 else 0
            pre_right = self.prefix[r][col2]
            res += (pre_right - pre_left)
        return res
