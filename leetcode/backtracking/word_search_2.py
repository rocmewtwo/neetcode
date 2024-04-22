# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/description/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build Trie
        word_dict = Trie()
        for word in words:
            word_dict.add(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        path = set()

        def dfs(r, c, curr, curr_str):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in path or
                    board[r][c] not in curr.children):
                return

            curr_str += board[r][c]
            curr = curr.children[board[r][c]]
            if curr.word:
                res.add(curr_str)

            path.add((r, c))
            dfs(r + 1, c, curr, curr_str)
            dfs(r - 1, c, curr, curr_str)
            dfs(r, c + 1, curr, curr_str)
            dfs(r, c - 1, curr, curr_str)
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, word_dict.root, "")
        return res
