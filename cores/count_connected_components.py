from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1) -> int:
        res = n1

        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return 0

        if self.rank[p2] > self.rank[p1]:  # r2 > r1
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]
        else:  # r1 >= r2
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        return 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for n1, n2 in edges:
            res -= uf.union(n1, n2)

        return res
