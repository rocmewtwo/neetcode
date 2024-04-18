# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        total = 0
        count = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                total -= arr[l]
                l += 1
            total += arr[r]
            if r - l + 1 == k and total / k >= threshold:
                count += 1
        return count
