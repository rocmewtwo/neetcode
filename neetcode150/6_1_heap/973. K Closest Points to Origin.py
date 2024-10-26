# 973. K Closest Points to Origin - Medium
# url: https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.pop_k_items(points, k)
        # return self.manage_k_items_list(points, k)

    # time complexity: heapify O(n), pop O(klogn) = O(n + klogn)
    # space complexity: O(n)
    def pop_k_items(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap: list = []
        for point in points:
            d = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(min_heap, (d, point))

        ans: List[List[int]] = []
        while k > 0:
            d, point = heapq.heappop(min_heap)
            k -= 1
            ans.append(point)

        return ans

    # manage maximum k items in a max_heap
    # if the heap is not full, push the item
    # if the heap is full, pop if the new item is smaller than the largest.
    # time complexity: O(nlogk), space complexity: O(k)
    def manage_k_items_list(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap: list = []

        for point in points:
            d = math.sqrt(point[0] ** 2 + point[1] ** 2)

            # if not full
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-d, point))
            else:  # full
                if d < -max_heap[0][0]:  # full and d is smaller than the largest
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-d, point))

        return [p for _, p in max_heap]


if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[1, 3], [-2, 2]], 1))  # [[-2, 2]]
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # [[3, 3], [-2, 4]]
