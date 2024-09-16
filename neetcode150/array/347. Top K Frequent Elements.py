# 347. Top K Frequent Elements - Medium
# url: https://leetcode.com/problems/top-k-frequent-elements/

from heapq import heapify, heappop, heappush
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucket(nums, k)
        # return self.k_elements_heap(nums, k)
        # return self.simple_heap(nums, k)

    # time: O(n)
    # space: O(n)
    def bucket(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]  # freq: [num1, num2, ...]

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

    # time: O(n + nlogk)
    # space: O(n)
    # O(n + nlogk) is typically preferred because it efficiently handles the case where ( k ) is much smaller than ( n )
    def k_elements_heap(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # {k: freq}
        heap = []  # manage k large min-heap

        for num, freq in count.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heappop(heap)
                heappush(heap, (freq, num))

        return [num for _, num in heap]

    # time: O(n + klogn)
    # space: O(n)
    def simple_heap(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-v, k) for k, v in freq.items()]
        heapify(heap)

        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(s.topKFrequent(nums=[1], k=1))
    print(s.topKFrequent(nums=[1, 2], k=2))
