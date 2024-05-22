# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/description/

from collections import defaultdict
from typing import List


# c3 -> c2 -> c1
# the direction in graph is already reversed. when we run topological sort, then res will be added in postorder
# the order will be like c1, c2, c3. The result is we expected.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for c2, c1 in prerequisites:
            adj_list[c2].append(c1)

        res = []
        path = set()
        visit = set()

        def dfs(c):
            if c in path:
                return False
            if c in visit:
                return True

            path.add(c)
            visit.add(c)
            for nei in adj_list[c]:
                if not dfs(nei):
                    return False
            res.append(c)
            path.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
