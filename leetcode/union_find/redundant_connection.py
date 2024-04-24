# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description/

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for i in range(len(edges) + 1)]

        def find(n1) -> int:
            p = parent[n1]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
