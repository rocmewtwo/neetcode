class SegmentTree:
    def __init__(self, L, R, val):
        # L == R default
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        self.range_max = val

        if L != R:
            M = (L + R) // 2
            self.left = SegmentTree(L, M, val)
            self.right = SegmentTree(M + 1, R, val)
            self.range_max = max(self.left.range_max, self.right.range_max)

    # time: O(logn)
    def update(self, index: int, val: int) -> None:
        # leaf node
        if self.L == self.R:
            self.range_max = val
            return

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.range_max = max(self.left.range_max, self.right.range_max)

    # time: O(logn)
    def range_query(self, L: int, R: int) -> int:
        if L > self.R or R < self.L:
            return 0

        if L <= self.L and self.R <= R:
            return self.range_max

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.range_query(L, R)
        elif R <= M:
            return self.left.range_query(L, R)
        else:
            return max(self.left.range_query(L, R), self.right.range_query(L, R))


nums = [1, 2, 3, 4, 5]
tree = SegmentTree(0, len(nums) - 1, 0)
for i in range(len(nums)):
    tree.update(i, nums[i])

print(tree.range_query(1, 3))
