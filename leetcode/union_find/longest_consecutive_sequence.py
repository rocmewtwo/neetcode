# 128. Longest Consecutive Sequence - Medium
# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return self.rank[p1]
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
            return self.rank[p1]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
            return self.rank[p2]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.use_union_find(nums)
        # return self.use_set(nums)

    # time: O(n), space: O(n)
    def use_union_find(self, nums: List[int]) -> int:
        num_index = {}
        uf = UnionFind(len(nums))
        max_len = 0

        for i, n in enumerate(nums):
            # record index without duplicate
            if n not in num_index:
                num_index[n] = i

                size = 1
                if n - 1 in num_index:
                    size = uf.union(num_index[n - 1], i)
                if n + 1 in num_index:
                    size = uf.union(num_index[n + 1], i)
                max_len = max(size, max_len)
        return max_len

    # time: O(n), space: O(n)
    def use_set(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in nums:
            # checking is the start of sequence -> prevent worse case to n^2
            if n - 1 not in num_set:
                l = 1
                while l + n in num_set:
                    l += 1
                max_len = max(max_len, l)
        return max_len
