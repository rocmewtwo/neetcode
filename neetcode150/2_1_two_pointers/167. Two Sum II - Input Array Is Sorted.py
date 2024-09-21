# 167. Two Sum II - Input Array Is Sorted - Medium
# url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum > target:
                r -= 1
            else:
                l += 1
