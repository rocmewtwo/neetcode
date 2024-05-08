# 46. Permutations
# https://leetcode.com/problems/permutations/description/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.remaining_permute(nums)
        # return self.choosed_set_permute(nums)

    def remaining_permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remaines, cur_perm):
            if not remaines:
                res.append(cur_perm.copy())
                return

            for i in range(len(remaines)):
                dfs(remaines[:i] + remaines[i+1:], cur_perm + [remaines[i]])

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
                if i not in choosed:
                    choosed.add(i)
                    dfs(cur_perm + [nums[i]])
                    choosed.remove(i)

        dfs([])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
