# 2261. K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/description/

from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        return self.using_trie(nums, k, p)
        # return self.rolling_hash(nums, k, p)
        # return self.enumerate_all(nums, k, p)

    # time: O(n^2)
    def using_trie(self, nums: List[int], k: int, p: int) -> int:
        trie = {}
        res = 0

        for i in range(len(nums)):
            cur = trie
            count = 0
            p_counter = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    p_counter += 1
                if p_counter > k:
                    break

                # find a new subarray
                if nums[j] not in cur:
                    cur[nums[j]] = {}
                    count += 1
                cur = cur[nums[j]]

            # count contain all subarrays that can be made from nums[i:j]
            res += count
        return res

    # time: O(n^2)
    def rolling_hash(self, nums: List[int], k: int, p: int) -> int:
        base = 201
        mod = 10**9 + 7
        res = set()

        for i in range(len(nums)):
            p_count = 0
            cur_hash = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    p_count += 1
                if p_count > k:
                    break

                cur_hash += (cur_hash * base + nums[j]) % mod
                if cur_hash not in res:
                    res.add(cur_hash)

        return len(res)

    # time: O(n^3), space: O(n^2)
    def enumerate_all(self, nums: List[int], k: int, p: int) -> int:
        res = set()

        for i in range(len(nums)):
            p_count = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    p_count += 1
                if p_count > k:
                    break
                res.add(tuple(nums[i: j + 1]))  # O(n)

        return len(res)


s = Solution()
print(s.countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2))
