class SegmentTree:
    def __init__(self, L, R, val):
        self.L = L  # left index of array
        self.R = R  # right index of array
        self.left = None
        self.right = None
        self.sum = val

        if L != R:
            M = (L + R) // 2
            self.left = SegmentTree(L, M, val)
            self.right = SegmentTree(M + 1, R, val)
            self.sum = self.left.sum + self.right.sum

    # time: O(logn)
    def update(self, index: int, val: int) -> None:
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum

    # time: O(logn)
    def range_query(self, L: int, R: int) -> int:
        # out range
        if L > self.R or R < self.L:
            return 0

        # out range, but overlap whole range
        if L <= self.L and self.R <= R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.range_query(L, R)
        elif R <= M:
            return self.left.range_query(L, R)
        else:
            return self.left.range_query(L, M) + self.right.range_query(M + 1, R)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    tree = SegmentTree(0, len(nums) - 1, 0)

    # O(nlogn)
    for i in range(len(nums)):
        tree.update(i, nums[i])

    print(tree.range_query(0, 4))
    print(tree.range_query(2, 4))
    print(tree.range_query(1, 3))
    print(tree.range_query(-1, 10))  # range covery whole array
