# 1. Two Sum - Easy
# url: https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], i]
            mapping[num] = i

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 6))  # [1, 2]
    print(s.twoSum([3, 3], 6))  # [0, 1]
