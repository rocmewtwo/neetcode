# Alien Dictionary
# https://neetcode.io/problems/foreign-dictionary

from collections import defaultdict
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        visit = set()
        path = set()
        res = []

        # topological sort
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True

            visit.add(node)
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            path.remove(node)
            return True

        char_set = {c for w in words for c in w}

        # build adj
        adj = defaultdict(list)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # invalid order
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w2[j]].append(w1[j])  # put pre to dst, w1 is pre of w2
                    break

        # for every char run top sort
        for c in char_set:
            if not dfs(c):
                return ""
        return "".join(res)


s = Solution()
print(s.foreignDictionary(["z", "o"]))
print(s.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
