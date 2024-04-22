# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    # for loop
    def search(self, word: str) -> bool:
        # if we face dot, search all children
        def dfs(curr, j):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(self.root, 0)

    # pure dfs
    def search(self, word: str) -> bool:
        # if we face dot, search all children
        def dfs(curr, i) -> bool:
            if i == len(word):
                return curr.word

            c = word[i]
            if c in curr.children:
                return dfs(curr.children[c], i + 1)
            elif c == '.':
                for child in curr.children.values():
                    if dfs(child, i + 1):
                        return True
            return False

        return dfs(self.root, 0)
