# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq


class MedianFinder:
    def __init__(self):
        # arr => [small][large]
        self.small = []
        self.large = []

    # add element to small, and move element to large
    def addNum(self, num: int) -> None:
        # add to small, large -> small
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        else:  # add to small, move one element to large
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))

    def findMedian(self) -> float:
        # we add element priorly to small, len(small) >= len(large)
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]


class MedianFinder2:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)  # O(logn)
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)  # O(logn)
            heapq.heappush(self.large, val)  # O(logn)

        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)  # O(logn)
            heapq.heappush(self.large, val)  # O(logn)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)  # O(logn)
            heapq.heappush(self.small, -val)  # O(logn)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]


class MedianFinder3:
    def __init__(self):
        # [small][large]
        self.small = []  # maxheap
        self.large = []  # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # swap max and min
        if self.small and self.large and -self.small[0] > self.large[0]:
            min_val = heapq.heappop(self.large)
            max_val = -heapq.heappop(self.small)
            heapq.heappush(self.large, max_val)
            heapq.heappush(self.small, -min_val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
