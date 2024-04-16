def kadanes(nums):
    # Kadane's Algorithm: O(n)
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(cur_sum, max_sum)  # update max sum

    return max_sum


def kadanes2(nums):
    # Kadane's Algorithm: O(n)
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)  # if negative, reset
        cur_sum += n
        max_sum = max(cur_sum, max_sum)  # update max sum

    return max_sum


def kadanes_sliding_windows(nums):
    # Return the left and right index of the max subarray sum,
    # Sliding window variation of Kadane's: O(n)
    max_sum, max_L, max_R = nums[0], 0, 0
    cur_sum = 0
    L = 0

    for R in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            L = R  # reset subarray

        cur_sum += nums[R]

        if cur_sum > max_sum:
            max_L = L
            max_R = R
            max_sum = cur_sum

    return [max_L, max_R]


if __name__ == "__main__":
    nums = [4, -1, 2, -7, 3, 4]
    print(kadanes(nums))
    print(kadanes_sliding_windows(nums))
