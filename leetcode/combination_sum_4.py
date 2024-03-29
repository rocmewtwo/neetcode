# 377. Combination Sum IV

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.top_down(nums, target)
        return self.bottom_up(nums, target)

    def bottom_up(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[total]

    def top_down(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(total) -> int:
            if total in dp:
                return dp[total]

            if total == target:
                return 1

            if total > target:
                return 0

            res = 0
            for n in nums:
                res += dfs(total + n)
            dp[total] = res
            return res

        return dfs(0)
