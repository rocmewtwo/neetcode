# Count Connected Components
# https://neetcode.io/problems/count-connected-components

from typing import List


class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, n1):
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p2] = p1
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for n1, n2 in edges:
            if uf.union(n1, n2):
                res -= 1
        return res
        # return len(set(dsu.findParent(x) for x in range(n)))
