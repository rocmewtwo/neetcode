from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List


class Solution:
    # worse case E = V^2
    # E*logE = E*logV^2 = 2E*logV = E*logV
    # time: O(E * logV) or O(E * logE)
    # space: O(E) for heap
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # build adj list
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))

        # compute shortest path
        shortest = {}
        min_heap = [(0, src)]  # cost, node
        while min_heap:
            w1, n1 = heappop(min_heap)

            if n1 in shortest:  # already find shortest path
                continue
            shortest[n1] = w1

            # push neighbor into heap
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heappush(min_heap, (w1 + w2, n2))

        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


s = Solution()
print(s.shortestPath(n=5, edges=[[0, 1, 10], [0, 2, 3], [2, 0, 1], [
      1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]], src=0))
