# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/description/

from typing import List
from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_med():
            if k % 2 == 0:
                return (w[k // 2 - 1] + w[k // 2]) / 2
            else:
                return w[k//2]
        w = SortedList()
        res = []

        for i in range(k):
            w.add(nums[i])
        res.append(get_med())

        for i in range(k, len(nums)):
            w.add(nums[i])  # O(logk)
            w.remove(nums[i - k])  # O(logk)
            res.append(get_med())
        return res
