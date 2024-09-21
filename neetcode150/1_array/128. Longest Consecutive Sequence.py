# 128. Longest Consecutive Sequence - medium
# url: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# time complexity: O(n), space complexity: O(n)
# outer loop: O(n), inner loop only run once for each sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in num_set:  # find a new sequence
                l = 1
                while num + l in num_set:  # extend length
                    l += 1
                max_len = max(max_len, l)
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(s.longestConsecutive([1, 2, 0, 1]))  # 3
