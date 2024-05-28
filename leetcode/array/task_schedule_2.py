# 2365. Task Scheduler II
# https://leetcode.com/problems/task-scheduler-ii/description/

from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0
        next_avaiable_days = {}

        for t in tasks:
            # can take task or set time to next avaiable days
            days = max(days + 1, next_avaiable_days.get(t, 0))
            next_avaiable_days[t] = days + space + 1

        return days
