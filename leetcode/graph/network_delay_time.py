# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # time: O(E*logV)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        # build adj list
        for s, d, w in times:
            adj_list[s].append((d, w))

        t = 0
        visit = set()
        min_heap = [(0, k)]
        while min_heap:
            w1, n1 = heappop(min_heap)
            if n1 in visit:
                continue

            visit.add(n1)
            t = w1
            for n2, w2 in adj_list[n1]:
                if n2 not in visit:
                    heappush(min_heap, (w1 + w2, n2))

        return t if len(visit) == n else -1


s = Solution()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
