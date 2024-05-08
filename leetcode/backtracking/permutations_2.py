# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/

from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.counter_permute(nums)
        # return self.remaining_permute(nums)
        # return self.choosed_set_permute(nums)

    def counter_permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []

        # counter condense array to prevent choose duplicate number
        counter = Counter(nums)
        # counter = {n: 0 for n in nums}
        # for n in nums:
        #     counter[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in counter:
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1
                    dfs()
                    counter[n] += 1
                    perm.pop()
        dfs()
        return res

    def remaining_permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(nums, perm):
            if not nums:
                res.append(perm)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                dfs(nums[:i] + nums[i + 1:], perm + [nums[i]])

        dfs(nums, [])
        return res

    def choosed_set_permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        choosed = set()

        def dfs(cur_perm):
            if len(cur_perm) == len(nums):
                res.append(cur_perm)
                return

            for i in range(len(nums)):
                if i in choosed:
                    continue

                # i - 1 in choosed -> first element subset
                # i - 1 not in choosed -> duplcate element -> skip
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in choosed:
                    continue

                choosed.add(i)
                dfs(cur_perm + [nums[i]])
                choosed.remove(i)

        nums.sort()
        dfs([])
        return res


s = Solution()
print(s.permuteUnique([1, 1, 2]))
