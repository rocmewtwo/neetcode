# 739. Daily Temperatures - Medium
# url: https://leetcode.com/problems/daily-temperatures/

from typing import List


# monotonic decreasing stack
# Time: O(n), Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # back check stack
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    # [1, 1, 4, 2, 1, 1, 0, 0]
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(s.dailyTemperatures([30, 60, 90, 50, 40, 80, 70, 60]))
    # [1,1,1,0]
    print(s.dailyTemperatures([30, 40, 50, 60]))
    # [1,1,0]
    print(s.dailyTemperatures([30, 60, 90]))
