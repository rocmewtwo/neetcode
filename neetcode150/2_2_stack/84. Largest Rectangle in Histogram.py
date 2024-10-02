# 84. Largest Rectangle in Histogram - Hard
# url: https://leetcode.com/problems/largest-rectangle-in-histogram/


from typing import List


# time complexity: O(n), space complexity: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        max_area = 0
        for i, h in enumerate(heights):
            start_index = i  # trace a index can go backward to extend histogram

            while stack and stack[-1][1] > h:  # the height can't extend anymore
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start_index = index  # can extend from index to i
            stack.append((start_index, heights[i]))

        # all the remaining heights can extend to the end
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(s.largestRectangleArea([2, 4]))  # 4
    print(s.largestRectangleArea([1, 1]))  # 2
    print(s.largestRectangleArea([2, 2]))  # 4
    print(s.largestRectangleArea([2, 1, 2]))  # 3
