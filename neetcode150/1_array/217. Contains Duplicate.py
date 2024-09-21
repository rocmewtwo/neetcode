# 217. Contains Duplicate - Easy
# url: https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.check_lenght(nums)
        # return self.check_set(nums)

    def check_lenght(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def check_set(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
