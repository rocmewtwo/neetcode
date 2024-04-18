# Find the length of longest subarray with the same
# value in each position: O(n)

# sliding window
def longestSubarray(nums):
    max_len = 0
    l = 0
    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r
        max_len = max(max_len, r - l + 1)
    return max_len


# array scan
def longestSubarray2(nums):
    max_len = 0
    cur_num = nums[0]
    cur_len = 0

    for n in nums:
        if cur_num != n:
            cur_len = 0
            cur_num = n
        cur_len += 1
        max_len = max(max_len, cur_len)
    return max_len


print(longestSubarray([4, 2, 2, 3, 3, 3]))
print(longestSubarray2([4, 2, 2, 3, 3, 3]))
