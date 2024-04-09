# 210. Course Schedule II

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)

        visit = set()
        path = set()  # detect cycle

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True

            visit.add(node)
            path.add(node)
            for nei in adj_list.get(node, []):
                if not dfs(nei):
                    return False
            sort_list.append(node)
            path.remove(node)
            return True

        sort_list = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return sort_list
