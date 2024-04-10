class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else 0) + \
                        (dp[i][j - 1] if j - 1 >= 0 else 0)

        return dp[m-1][n-1]


s = Solution()
print(s.uniquePaths(3, 7))
