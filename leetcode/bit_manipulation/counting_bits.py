# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == offset * 2:  # next round
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp
