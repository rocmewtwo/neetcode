# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    # time: O(n^2), space: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        for i in range(len(nums)):
            # skip duplicate
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # skip duplicate
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-1, 0, 1, 2, -1, -4, -1]))
