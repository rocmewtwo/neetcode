# 2696. Minimum String Length After Removing Substrings - Easy
# url: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# If we can change string in place, we can reduce space complexity to O(1).
# String in python is immutable. Maybe C++ or lower level language.
# time: O(n), space: O(n)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if stack and (c == "B" and stack[-1] == "A" or c == "D" and stack[-1] == "C"):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.minLength("ABFCACDB"))  # 2
    print(s.minLength("ACBBD"))  # 5
