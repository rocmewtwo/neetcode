# 721. Accounts Merge
# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, n1) -> int:
        p = self.parent[n1]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2) -> bool:
        p1, p2 = self.find(n1), self.find(n2)  # find roots

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    # union find
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # return self.union_find_merge(accounts)
        return self.dfs_merge(accounts)

    def union_find_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_index = {}

        # union idx of email
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_index:
                    uf.union(email_index[email], i)
                else:
                    email_index[email] = i

        # group: idx: email list
        mail_group = defaultdict(list)
        for email, idx in email_index.items():
            root = uf.find(idx)
            mail_group[root].append(email)

        res = []
        for i, emails in mail_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

    # N: number of accounts
    # K: max number of emails per user
    # time: O(NK) * N logK -> O(N * K * N * logK)
    # space: O(NK)
    def dfs_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(set)
        email_to_name = {}

        # build graph (adj list)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                adj_list[email].add(account[1])
                adj_list[account[1]].add(email)
                email_to_name[email] = name

        def dfs(email):
            visited.add(email)
            res = [email]
            for adj in adj_list[email]:
                if adj not in visited:
                    res += dfs(adj)
            return res

        # dfs on graph
        visited = set()
        res = []
        for email in adj_list:
            if email not in visited:
                local_res = dfs(email)
                res.append([email_to_name[email]] + sorted(local_res))
        return res
