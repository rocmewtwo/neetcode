# Problem: 7. Reverse Integer
# url: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium

import math


MININT = -2 ** 31
MAXINT = 2 ** 31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        return self.multiple_ten(x)
        # return self.store_digit(x)
        # return self.using_fmod(x)

    # time complexity: O(n)
    # space complexity: O(n)
    def store_digit(self, x: int) -> int:
        res = 0
        digits = []
        negative = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digits.append(x % 10)
            x = x // 10

        for i, t in enumerate(digits):
            res += t * 10 ** (len(digits) - i - 1)

        return res * negative if MININT <= res * negative <= MAXINT - 1 else 0

    # time complexity: O(n)
    # space complexity: O(1)
    # in this case, we don't need to store all digits
    # we can multiply 10 to res and add the last digit of x
    def multiple_ten(self, x: int) -> int:
        res = 0
        negative = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            res = res * 10 + x % 10
            x = x // 10

        return res * negative if MININT <= res * negative <= MAXINT - 1 else 0

    def using_fmod(self, x: int) -> int:
        res = 0

        while x != 0:
            digit = int(math.fmod(x, 10))  # python dumb: -1 % 10 = 9
            x = int(x / 10)  # python dumb: -1 / 10 = -1
            res = res * 10 + digit

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))  # 321
    print(s.reverse(-123))  # -321
    print(s.reverse(120))  # 21
    print(s.reverse(-12))  # -21
    print(s.reverse(0))  # 0
    print(s.reverse(1534236469))  # 0
    print(s.reverse(-2147483648))  # 0
    print(s.reverse(1563847412))  # 0
