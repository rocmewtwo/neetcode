# 1143. Longest Common Subsequence

class Solution:
    # time: O(m * n), space: O(m * n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # right bottom addding extra 0 for base case
        dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]

        # bottom up
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    # time: O(m * n), space: O(m * n)
    def longestCommonSubsequence_dfs_memo(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1 for j in range(n)] for i in range(m)]

        def dfs(i, j):
            # out range
            if i == len(text1) or j == len(text2):
                return 0

            if dp[i][j] >= 0:  # cache
                return dp[i][j]

            # calc dp
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = max(dfs(i, j + 1), dfs(i + 1, j))
            return dp[i][j]

        return dfs(0, 0)


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))
print(s.longestCommonSubsequence_dfs_memo("abcde", "ace"))
