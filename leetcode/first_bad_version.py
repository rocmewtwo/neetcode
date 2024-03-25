# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:  # stop at l == r: point to the first bad version
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid  # stay r pointer to bad version
            else:
                l = mid + 1  # if good version, move left pointer + 1

        return l
