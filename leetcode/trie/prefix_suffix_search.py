from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, idx):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.idx = idx


# with Trie
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for i, word in enumerate(words):
            for j in range(len(word)):
                w = word[j:] + "#" + word
                self.trie.add(w, i)

    def f(self, pref: str, suff: str) -> int:
        curr = self.trie.root
        for c in suff + '#' + pref:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.idx


# with Dict
class WordFilter_dict:
    def __init__(self, words: List[str]):
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        seen = set()

        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            if word not in seen:
                seen.add(word)
                for j in range(len(word)):
                    p = word[:j + 1]
                    s = word[j:]
                    self.prefix[p].add(i)
                    self.suffix[s].add(i)

    def f(self, pref: str, suff: str) -> int:
        overlap = self.prefix[pref] & self.suffix[suff]
        if not overlap:
            return -1
        return max(overlap)


w = WordFilter(["apple", "app", "arise"])
print(w.f("a", "e"))

w = WordFilter_dict(["apple", "app", "arise"])
print(w.f("a", "e"))
