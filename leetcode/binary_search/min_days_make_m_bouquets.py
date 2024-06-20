# 1482. Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description


from typing import List


class Solution:
    # time: O(nlogMax(bloomDay))
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def get_bouquets(day):
            count = 0
            num_bouquet = 0

            for d in bloomDay:
                if d > day:
                    count = 0
                else:
                    count += 1

                if count == k:
                    count = 0
                    num_bouquet += 1
            return num_bouquet

        if m * k > len(bloomDay):
            return -1

        l, r = 0, max(bloomDay)
        res = 0
        while l <= r:
            mid = l + (r - l) // 2

            if get_bouquets(mid) >= m:
                r = mid - 1
                res = mid
            else:
                l = mid + 1

        return res


s = Solution()

print(s.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))  # 3
print(s.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))  # -1
print(s.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))  # 12
