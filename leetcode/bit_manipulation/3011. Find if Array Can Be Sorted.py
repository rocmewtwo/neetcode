# 3011. Find if Array Can Be Sorted - Medium
# url: https://leetcode.com/problems/find-if-array-can-be-sorted/


from typing import List


def count_bits(n: int) -> int:
    return bin(n).count('1')


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = float('-inf')
        cur_min = cur_max = nums[0]

        for num in nums:
            if count_bits(num) == count_bits(cur_max):  # same group
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:  # find a new segment
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_max = cur_min = num

        # edge case to check the last group
        if prev_max > cur_min:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canSortArray([8, 4, 2, 30, 15]))  # true
    print(s.canSortArray([1, 2, 3, 4, 5]))  # true
    print(s.canSortArray([3, 16, 8, 4, 2]))  # false
