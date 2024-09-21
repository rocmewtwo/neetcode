# 15. 3Sum - Medium
# url: https://leetcode.com/problems/3sum/

from typing import List


# Time: O(n^2), Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # can quick remove duplicate

        # [-4, -1, -1, 0, 1, 2]
        # fix one n, and find two_sum = -n
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate
                i += 1
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:  # skip duplicate
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  # skip duplicate
                        r -= 1
                elif two_sum > target:
                    r -= 1
                else:
                    l += 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(s.threeSum([0, 1, 1]))  # []
print(s.threeSum([0, 0, 0]))  # [[0,0,0]]
print(s.threeSum([-2, 0, 0, 2, 2]))  # [[-2,0,2]]
