# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/

from collections import deque
from heapq import heapify, heappop, heappush
from typing import Counter, List


class Solution:
    # time: O(nlogk), n is the number of tasks, k is the distnct of tasks
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-v for v in count.values()]
        heapify(max_heap)

        t = 0
        q = deque()  # track task avaiable times
        while max_heap or q:
            t += 1

            # if max_heap is empty, set time to first avaiable time (optional)
            if not max_heap:
                t = q[0][1]

            if max_heap:
                freq = 1 + heappop(max_heap)  # drcrease freq
                if freq < 0:
                    q.append((freq, t + n))  # freq, avaiable time

            # check if any tasks are ready, push back to heap
            if q and t == q[0][1]:
                freq, _ = q.popleft()
                heappush(max_heap, freq)

        return t
