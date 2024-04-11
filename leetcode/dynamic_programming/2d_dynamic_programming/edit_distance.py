# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.bottom_up_minDistance(word1, word2)
        # return self.top_down_minDistance(word1, word2)

    # time: O(w1 + w2), space: O(w1 * w2)
    def bottom_up_minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word2) + 1)]
              for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][-1] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[-1][j] = len(word2) - j

        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1]
                                       [j], dp[i + 1][j + 1])
        return dp[0][0]

    # time: O(w1 + w2), space: O(w1 * w2)
    def top_down_minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for j in range(len(word2))] for i in range(len(word1))]

        def dfs(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j

            if dp[i][j] >= 0:  # cache
                return dp[i][j]

            # equal
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            remove = 1 + dfs(i + 1, j)
            insert = 1 + dfs(i, j + 1)
            replace = 1 + dfs(i + 1, j + 1)
            dp[i][j] = min(remove, insert, replace)
            return dp[i][j]

        return dfs(0, 0)


s = Solution()
print(s.top_down_minDistance("horse", "ros"))
print(s.top_down_minDistance("intention", "execution"))
print(s.top_down_minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"))
