# 670. Maximum Swap - Medium
# url: https://leetcode.com/problems/maximum-swap/


# The leading digit is siginicant position, if we swap a bigger digit, then we can get a bigger number.
# if we have a number, and split into digits d1 d2 d3 d4
# for d1, we find a max value max_d from d2 to d4, and swap max_d to d1 -> num1
# for d2, we find a max value max_d from d3 to d4, and swap max_d to d2 -> num2
# for d3, what is the max value we can get from d4 -> num3
# the max value will be max(num, num1, num2, num3)

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        return self.two_pointer_maximumSwap(num)
        # return self.greedy_maximumSwap(num)

    def greedy_maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        max_index = len(nums) - 1
        cur_max = num
        for i in range(len(nums) - 1, -1, -1):
            copy_nums = nums.copy()
            copy_nums[i], copy_nums[max_index] = copy_nums[max_index], copy_nums[i]
            cur_max = max(cur_max, int("".join(copy_nums)))

            if nums[i] > nums[max_index]:
                max_index = i
        return cur_max

    def two_pointer_maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        max_i = len(nums) - 1
        si, sj = 0, 0

        for i in reversed(range(len(nums))):
            if nums[i] > nums[max_i]:  # update the current max index
                max_i = i
            # if we find a smaller digit, we store the indices of current max and the current value
            elif nums[i] < nums[max_i]:
                si, sj = i, max_i
        nums[si], nums[sj] = nums[sj], nums[si]
        return int("".join(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSwap(2736))  # 7236
    print(s.maximumSwap(9973))  # 9973
