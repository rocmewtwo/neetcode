from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lis_binary_search(nums)
        # return self.lis_bottom_up(nums)

    # time: O(nlogn), space: O(n)
    def lis_binary_search(self, nums: List[int]) -> int:
        ans = []  # this ans possible not the lis, we only caculate len of subsequence
        max_len = 0
        ans.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                # find smallest element >= nums[i]
                l = 0
                r = len(ans) - 1
                while l < r:
                    m = (l + r) // 2  # (r - l) // 2 + l
                    if nums[i] > ans[m]:  # target in m+1 to r
                        l = m + 1
                    else:  # num <= mid, target in l to m
                        r = m
                ans[l] = nums[i]
            max_len = max(max_len, len(ans))
        # print(ans)
        return len(ans)

    # time: O(n^2), space: O(n)
    def lis_bottom_up(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)


s = Solution()
nums = [1, 7, 8, 4, 5, 6, -1, 9]
print(s.lis_binary_search(nums))
print(s.lis_bottom_up(nums))
