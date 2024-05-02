# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/description/

import heapq
from typing import List


class Median:
    def __init__(self):
        self.small, self.large = [], []

    # O(logk)
    def add(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))

    # O(k)
    def remove(self, num):
        # the len(small) == len(large) or len(small) == len(large) + 1
        # num in small
        if num <= -self.small[0]:
            if num == -self.small[0]:
                heapq.heappop(self.small)
            else:
                self.small.remove(-num)
                heapq.heapify(self.small)

            if len(self.small) < len(self.large):
                heapq.heappush(self.small, -heapq.heappop(self.large))

        else:  # num in large
            if num == self.large[0]:
                heapq.heappop(self.large)
            else:
                self.large.remove(num)
                heapq.heapify(self.large)

            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large, -heapq.heappop(self.small))

    # O(1)
    def get(self):
        # print(self.small, self.large)
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        helper = Median()  # med helper

        # add k numbers
        for i in range(k):
            helper.add(nums[i])
        res.append(helper.get())

        # move window to the end
        # remove: O(nk)
        for i in range(k, len(nums)):
            helper.add(nums[i])
            helper.remove(nums[i - k])
            res.append(helper.get())

        return res
