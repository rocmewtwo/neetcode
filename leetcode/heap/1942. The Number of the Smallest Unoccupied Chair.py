# 1942. The Number of the Smallest Unoccupied Chair - Medium
# url: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import heapq
from typing import List


# time: O(nlogn), sorting, push and pop for n elements
# space: O(n), used_chars and available_chars
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])  # sort index by start time

        used_chars = []  # (leave time, occupied chair)
        available_chars = [i for i in range(len(times))]  # available chars

        for i in indexes:
            arrival_time, leave_time = times[i]

            # clean with leave time
            while used_chars and used_chars[0][0] <= arrival_time:
                _, chair = heapq.heappop(used_chars)
                # push back to available chars
                heapq.heappush(available_chars, chair)

            chair = heapq.heappop(available_chars)
            heapq.heappush(used_chars, (leave_time, chair))

            if i == targetFriend:
                return chair


if __name__ == "__main__":
    s = Solution()
    print(s.smallestChair([[1, 4], [2, 3], [4, 6]], 1))  # 1
    print(s.smallestChair([[3, 10], [1, 5], [2, 6]], 0))  # 2
    print(s.smallestChair([[3, 10], [1, 5], [2, 6]], 2))  # 1
