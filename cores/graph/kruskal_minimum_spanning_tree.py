from typing import List
from heapq import heappush, heappop


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, n1) -> None:
        p = self.parent[n1]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


# Given an list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
# time: O(ElogV), space: O(E)
def minimumSpanningTree(n, edges) -> List[List[int]]:
    heap = []
    for n1, n2, w in edges:
        heappush(heap, (w, n1, n2))

    uf = UnionFind(n)
    mst = []
    while len(mst) < n - 1:  # len of mst = N - 1
        w, n1, n2 = heappop(heap)  # O(logV)
        if not uf.union(n1, n2):  # check cycle if adding this edge, O(logV) or O(1)
            continue
        mst.append([n1, n2])
    return mst


print(minimumSpanningTree(n=5, edges=[[0, 1, 10], [0, 2, 3], [
      1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]))
