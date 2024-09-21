# 238. Product of Array Except Self - Medium
# url: https://leetcode.com/problems/product-of-array-except-self/

from typing import List


# nums[i] = prefix[i] * suffix[i]
# time: O(n), space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
    print(s.productExceptSelf([1, 2, 3, 4, 5]))  # [120,60,40,30,24]
