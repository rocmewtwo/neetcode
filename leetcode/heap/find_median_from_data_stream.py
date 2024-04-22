import heapq


class MedianFinder:
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
