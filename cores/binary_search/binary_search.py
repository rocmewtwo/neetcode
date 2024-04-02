from typing import List


def binary_search(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        # m = l + ((r - l) // 2) # if l and r are very large, other language will have overflow.
        if target > arr[m]:
            l = m + 1
        elif target < arr[m]:
            r = m - 1
        else:
            return m

    return -1


arr = [1, 3, 3, 4, 5, 6, 7, 8]  # sorted array
print(binary_search(arr, 6))
print(binary_search(arr, 2))
