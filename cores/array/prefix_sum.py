class PrefixSum:
    # time: O(n)
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    # time: O(1)
    def rangeSum(self, left, right):
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left


prefixSum = PrefixSum([2, -1, 3, -3, 4])
print(prefixSum.rangeSum(1, 3))
print(prefixSum.rangeSum(0, 3))
print(prefixSum.rangeSum(1, 4))
