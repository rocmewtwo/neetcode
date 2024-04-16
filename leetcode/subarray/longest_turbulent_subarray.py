# 978. Longest Turbulent Subarray

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        max_len = 1
        prev = ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                max_len = max(max_len, r - l + 1)
                prev = "<"
                r += 1
            elif arr[r - 1] > arr[r] and prev != ">":
                max_len = max(max_len, r - l + 1)
                prev = ">"
                r += 1
            else:
                # r + 1, prevent equal stuck loop
                r = r if arr[r - 1] != arr[r] else r + 1
                l = r - 1
                prev = ""

        return max_len


s = Solution()
# 9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9
print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
