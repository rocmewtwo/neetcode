# the concep of a tree:
# 1. start one node and then visit to all nodes
# 2. the visit can't have cycle

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # build adj list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(node, prev):  # we don't have direct graph, we need a prev to prevent internal loop
            # cycle
            if node in visit:
                return False

            visit.add(node)
            # visit adj nodes
            for adj_node in adj[node]:
                if adj_node != prev:  # not visit back
                    if not dfs(adj_node, node):
                        return False
            return True

        # also check do we have non-connective nodes
        return dfs(0, -1) and len(visit) == n
