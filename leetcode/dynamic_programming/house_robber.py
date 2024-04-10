from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + nums[i])
        return dp[1]

    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + n)
        return dp[1]


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
