# 2707. Extra Characters in a String - Medium
# url: https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List


# why can't we use greedy?
# greedy will not work because we need to consider all possible words
# abcdef, [abc, bcdef]
# if we use abc, then extra char is 3 (def)
# if we skip a, then extra char is 1 (a)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            self.addWord(word)

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        return self.memoization_with_trie(s, dictionary)
        # return self.memoization(s, dictionary)

    # time complexity: O(n * n)
    # dfs -> n, inner loop -> n
    def memoization_with_trie(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        dp = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip curr char
            curr = trie.root
            for j in range(i, len(s)):  # start from i, and find all possible words
                if s[j] not in curr.children:  # can't find any prefix starting from s[j]
                    break
                curr = curr.children[s[j]]
                if curr.end:  # if we found a word in dictionary
                    res = min(res, dfs(j+1))

            dp[i] = res
            return dp[i]
        return dfs(0)

    # time complexity: O(n * n * n) = O(n^3)
    # dfs -> n, inner loop -> n, slicing substring -> n
    # we can optimize slicing substring by using trie
    def memoization(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip curr char
            for j in range(i, len(s)):  # start from i, and find all possible words
                if s[i:j+1] in dictionary:
                    res = min(res, dfs(j+1))

            dp[i] = res
            return dp[i]
        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    print(s.minExtraChar(
        s="leetscode",
        dictionary=["leet", "code", "leetcode"]))  # 1

    print(s.minExtraChar(
        s="sayhelloworld",
        dictionary=["hello", "world"]))  # 3

    print(s.minExtraChar(
        s="abcdef",
        dictionary=["abc", "bcdef"]))  # 1

    print(s.minExtraChar(
        s="dwmodizxvvbosxxw",
        dictionary=["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo", "cehy", "tskz", "ds", "kzbu"]))  # 7
