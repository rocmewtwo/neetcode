from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums) -> int:
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(n + rob1, rob2)
            return rob2

        # nums[0] if only one element
        return max(nums[0], rob1(nums[1:]), rob1(nums[:-1]))
