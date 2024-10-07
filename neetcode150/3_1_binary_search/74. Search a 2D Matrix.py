# 74. Search a 2D Matrix - Medium
# url: https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search_1d(matrix, target)

    # time complexity: O(logn), space complexity: O(1)
    def search_1d(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = (r - l) // 2 + l
            row = m // COLS
            col = m % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
    print(s.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
    print(s.searchMatrix([[1]], 1))  # True
    print(s.searchMatrix([[1]], 2))  # False
