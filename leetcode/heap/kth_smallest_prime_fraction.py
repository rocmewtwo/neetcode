# 786. K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return self.maintain_heap(arr, k)
        # return self.brute_force(arr, k)

    # time: O(nlogn + klogn) -> O((n+k) * logn)
    def maintain_heap(self, arr: List[int], k: int) -> List[int]:
        heap = []

        # O(nlogn)
        for i in range(len(arr) - 1):
            heappush(heap, (arr[i] / arr[-1], i, len(arr) - 1))

        '''
            can push
            0 1 2 3  4  5
                        r
                  l r-1
        '''
        # O(klogn)
        for _ in range(k):
            _, l, r = heappop(heap)
            if l < r - 1:
                heappush(heap, (arr[l] / arr[r - 1], l, r - 1))

        return [arr[l], arr[r]]

    # time: O(n^2)
    def brute_force(self, arr: List[int], k: int) -> List[int]:
        f = []
        # O(n^2)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                f.append((arr[i] / arr[j], arr[i], arr[j]))

        heapify(f)  # O(n^2)
        res = None
        for i in range(k):  # O(k * logn^2) -> O(k *logn)
            res = heappop(f)

        return res[1:]


s = Solution()
print(s.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
