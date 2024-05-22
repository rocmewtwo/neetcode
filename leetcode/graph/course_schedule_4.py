# 1462. Course Schedule IV
# https://leetcode.com/problems/course-schedule-iv/description/

from collections import defaultdict
from typing import List


class Solution:
    # n nodes, each dfs take nodes + edges O(n + p) -> build pre_map O(n * (p + n))
    # check queries -> O(q * 1)
    # total time complexity: O(n*(p + n) + q)
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adj
        adj_list = defaultdict(list)
        pre_map = defaultdict(set)
        for c2, c1 in prerequisites:
            adj_list[c2].append(c1)

        # build path from c
        def dfs(c):
            if c not in pre_map:
                path = set()
                for nei in adj_list[c]:
                    path |= dfs(nei)
                pre_map[c] |= path  # union
                pre_map[c].add(c)
            return pre_map[c]

        for i in range(numCourses):
            dfs(i)
        # print(pre_map)

        res = []
        # c2 -> c1
        # pre_map[c2] should be (c1, c2)
        for c2, c1 in queries:
            res.append(c1 in pre_map[c2])
        return res


s = Solution()
print(s.checkIfPrerequisite(numCourses=2,
      prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))
print(s.checkIfPrerequisite(numCourses=3, prerequisites=[
      [1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))


'''
    2
  1  3
  0

  2: (0, 1, 2, 3), 1: (0, 1), 0: (0), 3: (3)
'''
print(s.checkIfPrerequisite(numCourses=4,
      prerequisites=[[1, 0], [2, 1], [2, 3]], queries=[[0, 1], [1, 0]]))
