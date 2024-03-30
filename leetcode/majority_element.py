# 169. Majority Element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.moore(nums)
        # return self.counter(nums)

    # time: O(n) space: O(1)
    def moore(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            # if n == res:
            #     count += 1
            # else:
            #     count -= 1
        return res

    # time: O(n) space: O(n)
    def counter(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

            if count[n] > len(nums) / 2:
                return n
