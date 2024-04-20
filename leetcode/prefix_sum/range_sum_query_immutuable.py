# 303. Range Sum Query - Immutable

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left
