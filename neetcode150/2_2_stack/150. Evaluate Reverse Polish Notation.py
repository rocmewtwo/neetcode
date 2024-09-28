# 150. Evaluate Reverse Polish Notation - Medium
# url: https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # 6
