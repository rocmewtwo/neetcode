# 502. IPO - Hard
# https://leetcode.com/problems/ipo/description/

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = [] # only put into when w >= capital
        min_capital = [(c, p) for p, c in zip(profits, capital)]
        heapify(min_capital)

        for i in range(k):
            # put into max_profit heap if w >= capital
            while min_capital and w >= min_capital[0][0]:
                c, p = heappop(min_capital)
                heappush(max_profit, -p)

            if not max_profit:
                break

            w += -heappop(max_profit)
        return w