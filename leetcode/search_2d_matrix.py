from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return self.search_row_col(matrix, target)
        return self.search_1d_array(matrix, target)

    def search_row_col(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        # compare row
        while top <= bottom:
            row_mid = (top + bottom) // 2
            if target > matrix[row_mid][-1]:
                top = row_mid + 1
            elif top != bottom and target < matrix[row_mid][0]:
                bottom = row_mid - 1
            else:
                break  # row_mid is correct row

        if not (top <= bottom):
            return False

        left, right = 0, COLS - 1
        # compare cols
        while left <= right:
            col_mid = (left + right) // 2
            # compare col
            if target > matrix[row_mid][col_mid]:
                left = col_mid + 1
            elif target < matrix[row_mid][col_mid]:
                right = col_mid - 1
            else:
                return True
        return False

    def search_1d_array(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            mid_row, mid_col = divmod(mid, COLS)

            if target < matrix[mid_row][mid_col]:
                r = mid - 1
            elif target > matrix[mid_row][mid_col]:
                l = mid + 1
            else:
                return True
        return False
