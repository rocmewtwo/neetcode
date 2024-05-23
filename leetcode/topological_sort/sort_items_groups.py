# 1203. Sort Items by Groups Respecting Dependencies - Hard
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/

from collections import defaultdict
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # assgin group id to -1 (indepent group)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        print(f"{group=}")

        # build item adj
        # pre element put to dst like reversed edge
        item_adj = defaultdict(list)  # items dependency
        group_adj = defaultdict(list)  # group dependency
        for i in range(n):
            for pre in beforeItems[i]:
                item_adj[i].append(pre)
                if group[i] != group[pre]:
                    group_adj[group[i]].append(group[pre])

        print(f"{item_adj=}")
        print(f"{group_adj=}")

        # top_sort, sort group and sort items to get the correct relative position
        sort_items = self.top_sort(item_adj, n)
        sort_groups = self.top_sort(group_adj, m)
        print(f"{sort_items=}")
        print(f"{sort_groups=}")

        # check items or group has cycle
        if not sort_items or not sort_groups:
            return []

        # build group_id : [sorted items]
        group_items = defaultdict(list)
        for i in sort_items:
            group_items[group[i]].append(i)
        print(f"{group_items=}")

        # map sorted items into sorted group
        ans = []
        for g in sort_groups:
            ans.extend(group_items[g])
        return ans

    def top_sort(self, adj, n):
        visit = set()
        path = set()
        res = []

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True

            path.add(i)
            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            res.append(i)
            path.remove(i)
            return True

        for i in range(n):
            if not dfs(i):
                return False

        return res
