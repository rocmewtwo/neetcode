# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # time: O(ElogV) -> O(n^2 * logn^2) -> O(n^2 * logn)
    # space: O(E) -> O(n^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # build adj list
        adj = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, d))
                adj[j].append((i, d))

        # prim's
        heap = [(0, 0)]
        res = 0
        visit = set()
        while len(visit) < N:
            w1, n1 = heappop(heap)
            if n1 in visit:
                continue

            visit.add(n1)
            res += w1

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heappush(heap, (w2, n2))

        return res
