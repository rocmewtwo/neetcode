from typing import List


# Union-Find cycle detection works for undirected graphs.
# Topological Sort cycle detection works for directed graph.
# This problem is directed graph, we can't use union find
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            adj_list[src].append(dst)

        visit = set()
        path = set()  # dfs visiting path (used to detect cycle)

        def dfs(node) -> bool:
            if node in path:
                return False  # cycle

            if node in visit:
                return True

            path.add(node)
            visit.add(node)
            for nei in adj_list.get(node, []):
                if not dfs(nei):
                    return False  # cycle
            path.remove(node)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
