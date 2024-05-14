# 1514. Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/description/

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # time: O(ElogV)
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # build adj list
        adj = defaultdict(list)
        for (s, d), p in zip(edges, succProb):
            adj[s].append((d, p))
            adj[d].append((s, p))

        # compute shortest path
        max_heap = [(-1, start_node)]
        visit = set()
        while max_heap:
            p1, n1 = heappop(max_heap)

            if n1 in visit:
                continue
            visit.add(n1)

            if n1 == end_node:
                return -p1

            for d2, p2 in adj[n1]:
                if d2 not in visit:
                    heappush(max_heap, (p1 * p2, d2))

        return 0
