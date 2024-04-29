import bisect


def bisec_left(nums, val) -> int:
    l = 0
    r = len(nums)
    while l < r:
        m = (l + r) // 2
        if val > nums[m]:  # if greater, move left
            l = m + 1
        else:  # val <= nums[m]
            r = m
    return l


def bisec_right(nums, val) -> int:
    l = 0
    r = len(nums)

    l = 0
    r = len(nums)
    while l < r:
        m = (l + r) // 2
        if val >= nums[m]:  # if greater or equal, move left
            l = m + 1
        else:
            r = m
    return l


nums = [1, 5, 9, 13, 17]
print(bisec_left(nums, 7), bisect.bisect_left(nums, 7))
print(bisec_right(nums, 7), bisect.bisect_right(nums, 7))

nums = [1, 5, 5, 5, 17]
print(bisec_left(nums, 5), bisect.bisect_left(nums, 5))
print(bisec_right(nums, 5), bisect.bisect_right(nums, 5))
