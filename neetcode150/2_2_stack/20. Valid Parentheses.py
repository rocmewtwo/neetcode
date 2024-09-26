# 20. Valid Parentheses - Easy
# url: https://leetcode.com/problems/valid-parentheses/

class Solution:
    # Time: O(n), Space: O(n)
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
            else:  # closing bracket
                if not stack or mapping[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack  # if stack is empty, return True, else False


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([)]"))  # False
    print(s.isValid("{[]}"))  # True
