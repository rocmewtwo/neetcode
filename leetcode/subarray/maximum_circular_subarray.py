# 918. Maximum Sum Circular Subarray

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min, cur_max = 0, 0
        min_sum, max_sum = nums[0], nums[0]
        total = 0

        for n in nums:
            cur_min = min(cur_min + n, n)
            min_sum = min(min_sum, cur_min)
            cur_max = max(cur_max + n, n)
            max_sum = max(max_sum, cur_max)
            total += n

        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)


s = Solution()
print(s.maxSubarraySumCircular([1, -2, 3, -2]))
print(s.maxSubarraySumCircular([5, -3, 5]))
print(s.maxSubarraySumCircular([-3, -3, -5]))  # all negative case
