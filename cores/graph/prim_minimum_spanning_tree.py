from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # time: O(ElogV), space: O(E)
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # build adj
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))
            adj[d].append((s, w))

        # compute spaning tree
        heap = [(0, 0)]  # (w, s)
        visited = set()
        mst = 0

        while len(visited) < n:  # min tree edge -> e = N - 1
            w1, n1 = heappop(heap)
            if n1 in visited:
                continue

            visited.add(n1)
            mst += w1

            # visit neighbors
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    # only put weight (Dijkstra put w1 + w2)
                    heappush(heap, (w2, n2))

        return mst if len(visited) == n else -1


s = Solution()
print(s.minimumSpanningTree(n=5, edges=[[0, 1, 10], [0, 2, 3], [
      1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]))
