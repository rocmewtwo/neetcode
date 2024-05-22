# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree - Hard
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

from typing import Dict, List
from collections import defaultdict
from heapq import heappop, heappush


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, n1) -> int:
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


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        return self.using_kruskal_algorithm(n, edges)
        # return self.using_prims_algorithm(n, edges)

    def build_adj_list(self, edges) -> Dict[int, List[int]]:
        adj_list = defaultdict(list)

        for n1, n2, w in edges:
            adj_list[n1].append((w, n2))
            adj_list[n2].append((w, n1))

        return adj_list

    # if we count uf operation as O(E), total time complexity is O(E) * O(MST) = O(E) * O(ElogV)
    # if we uf path compression many time, UF operations are assumed to be approx O(1)
    # total time complexity is O(E) * O(MST) = O(E) * O(E) = O(E^2)
    def using_kruskal_algorithm(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)  # [n1, n2, weight, original_index]
        edges.sort(key=lambda e: e[2])  # O(ElogE)

        uf = UnionFind(n)
        mst = 0
        # Kruskal compute mst value
        for n1, n2, w, i in edges:
            if uf.union(n1, n2):  # can span tree
                mst += w

        critical, pseudo = [], []
        for n1, n2, weight_i, i in edges:
            # ignore i edge
            uf = UnionFind(n)
            mst2 = 0
            # Kruskal compute mst value
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):  # can span tree
                    mst2 += w
            if max(uf.rank) != n or mst2 > mst:
                critical.append(i)
                continue

            # if not critical -> we want to test this i edge is a pseudo edge
            uf = UnionFind(n)
            mst2 = weight_i
            uf.union(n1, n2)
            # Kruskal compute mst value
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    mst2 += w

            if mst == mst2:
                pseudo.append(i)

        return [critical, pseudo]

    def using_prims_algorithm(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # time: O(ElogV)
        def prims(n, adj_list, init_edge=[], ignore_edge=[]):
            min_heap = []
            visit = set()
            mst = 0

            if init_edge:  # add init edge, add edge, and add neighbors of n1 and n2
                n1, n2, w = init_edge
                mst += w
                visit.add(n1)
                visit.add(n2)

                for w, nei in adj_list[n1]:
                    if nei not in visit:
                        heappush(min_heap, (w, nei))

                for w, nei in adj_list[n2]:
                    if nei not in visit:
                        heappush(min_heap, (w, nei))
            else:
                min_heap.append((0, 0))  # start from 0

            while min_heap:
                w1, n1 = heappop(min_heap)

                if n1 in visit:
                    continue

                visit.add(n1)
                mst += w1
                for w2, n2 in adj_list[n1]:
                    if n1 in ignore_edge and n2 in ignore_edge:
                        continue

                    if n2 not in visit:
                        heappush(min_heap, (w2, n2))

            return mst if len(visit) == n else float("inf")

        adj_list = self.build_adj_list(edges)
        mst = prims(n, adj_list)
        critical, pseudo = [], []

        # O(E * ElogV)
        for i, edge in enumerate(edges):
            if prims(n, adj_list, ignore_edge=edge[:2]) > mst:
                critical.append(i)
            elif prims(n, adj_list, init_edge=edge) == mst:
                pseudo.append(i)

        return [critical, pseudo]


s = Solution()
print(s.using_prims_algorithm(n=5, edges=[[0, 1, 1], [
      1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]))

print(s.using_kruskal_algorithm(n=5, edges=[[0, 1, 1], [
      1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]))
