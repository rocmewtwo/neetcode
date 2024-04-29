# 2407. Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/description/

from typing import List
from neetcode.cores.tree.segment_tree_range_max import SegmentTree


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        res = 1
        n = max(nums)
        tree = SegmentTree(0, n, 0)

        for num in nums:
            l = tree.range_query(max(0, num - k), max(0, num - 1))
            tree.update(num, l + 1)
            res = max(res, l + 1)
        return res
