# 139. Word Break - Medium
# url: https://leetcode.com/problems/word-break/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True


class Solution:
    # Time complexity: O(n^2)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(wordDict)
        dp = {}

        def dfs(i) -> bool:
            if i == len(s):
                return True
            if i in dp:
                return dp[i]

            curr = trie.root
            for j in range(i, len(s)):
                c = s[j]
                if c not in curr.children:  # no word can be formed
                    break
                curr = curr.children[c]
                if curr.end:
                    if dfs(j + 1):  # find substring j + 1 can break with dictionary
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # True
    print(s.wordBreak("catsandog", [
          "cats", "dog", "sand", "and", "cat"]))  # False
