# 875. Koko Eating Bananas - Medium
# url: https://leetcode.com/problems/koko-eating-bananas/


import math
from typing import List


# guess speed k from 1 to max(piles)
# using binary search to cut the half part
# time complexity: O(nlogm), where n is the length of piles, m is the max value of piles
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # can eat all with hours <= h
        def can_finish_all(speed) -> bool:
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / speed)
            return total_hours <= h

        l, r = 1, max(piles)
        res = r
        while l <= r:
            speed = (r - l) // 2 + l
            if can_finish_all(speed):  # O(n)
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))  # 4
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))  # 23
