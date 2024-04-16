# 209. Minimum Size Subarray Sum

import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = math.inf
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r - l)
                total -= nums[l]
                l += 1
        return min_len if min_len != math.inf else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(15, [1, 2, 3, 4, 5]))
