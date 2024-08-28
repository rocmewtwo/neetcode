# 650. 2 Keys Keyboard - Medium
# url: https://leetcode.com/problems/2-keys-keyboard/


class Solution:
    def minSteps(self, n: int) -> int:
        return self.bottom_up(n)
        # return self.top_down(n)

    # time complexity: O(n^2)
    # space complexity: O(n)
    # 1 --- x --- n
    # if we have factor x, we can copy x times and paste n // x times
    # formula: dp[x] + n // x
    # loop through all factors of n to find the minimum steps
    def bottom_up(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, i + n // 2):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]

    # time complexity: O(n^2), because we hve count and copied, and we can have n * n states
    # space complexity: O(n^2)
    def top_down(self, n: int) -> int:
        cache = {}

        def helper(count, copied):
            # base case
            if count == n:
                return 0
            if count > n:
                return float('inf')
            if (count, copied) in cache:
                return cache[(count, copied)]

            # paste
            res1 = 1 + helper(count + copied, copied)
            # copy and past
            res2 = 2 + helper(count + count, count)
            cache[(count, copied)] = min(res1, res2)
            return cache[(count, copied)]

        if n == 1:
            return 0
        return 1 + helper(1, 1)


s = Solution()
print(s.minSteps(3))  # 3
print(s.minSteps(1))  # 0
print(s.minSteps(4))  # 4
print(s.minSteps(5))  # 5
print(s.minSteps(6))  # 5
print(s.minSteps(7))  # 7
print(s.minSteps(8))  # 6
