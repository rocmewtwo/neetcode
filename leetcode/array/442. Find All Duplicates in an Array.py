# 442. Find All Duplicates in an Array - Medium
# url: https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return self.counter(nums)
        # return self.mark_sign(nums)

    # can deal with multiple duplicates
    # https://www.geeksforgeeks.org/duplicates-array-using-o1-extra-space-set-2/?ref=oin_asr2
    def counter(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        # make all number to index
        # to prevent overflow, we use n to get the original number
        for i in range(len(nums)):
            nums[i] -= 1

        for num in nums:
            index = num % n
            nums[index] += n

        # print(nums)
        for i in range(len(nums)):
            if nums[i] >= 2 * n:
                res.append(i + 1)
        return res

    # can only deal with one duplicate, appear once or twice
    def mark_sign(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            # find duplicate -> find index is already negetive
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(index + 1)
            # mark sign
            else:
                nums[index] = -nums[index]

        return res


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2,3]
print(s.findDuplicates([1, 1, 2]))  # [1]
print(s.findDuplicates([1]))  # []
print(s.findDuplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))  # [1, 2, 3]
print(s.findDuplicates([2, 1]))  # []
print(s.findDuplicates([1, 1]))  # [1]
