# Remove all redundant parenthesis - Hard
# url: https://www.geeksforgeeks.org/remove-redundant-parentheses-algebraic-expression/

# For example:
# "1*(2+(3*(4+5)))" => "1*(2+3*(4+5))"
# "2 + (3 / -5)" => "2 + 3 / -5"
# "x+(y+z)+(t+(v+w))" => "x+y+z+t+v+w"

'''
cases:
+
    a + (b + c) == a + b + c, yes
    a + (b * c) == a + b * c, yes
    a + (b - c) == a + b - c, yes
    a + (b / c) == a + b / c, yes

    (b + c) + a == b + c + a, yes
    (b * c) + a == b * c + a, yes
    (b - c) + a == b - c + a, yes
    (b / c) + a == b / c + a, yes

-
    a - (b + c) == a - b - c, yes
    a - (b * c) == a - b * c, yes
    a - (b - c) != a - b - c, no #####
    a - (b / c) == a - b / c, yes

    (b + c) - a == b + c - a, yes
    (b * c) - a == b * c - a, yes
    (b - c) - a == b - c - a, yes
    (b / c) - a == b / c - a, yes

*
    a * (b + c) != a * b + c, no #####
    a * (b * c) == a * b * c, yes
    a * (b - c) != a * b - c, no
    a * (b / c) == a * b / c, yes

    (b + c) * a != b + c * a, no #####
    (b * c) * a == b * c * a, yes
    (b - c) * a != b - c * a, no #####
    (b / c) * a == b / c * a, yes

/
    a / (b + c) != a / b + c, no #####
    a / (b * c) == a / b * c, yes
    a / (b - c) != a / b - c, no #####
    a / (b / c) == a / b / c, yes

    (b + c) / a != b + c / a, no #####
    (b * c) / a == b * c / a, yes
    (b - c) / a != b - c / a, no #####
    (b / c) / a == b / c / a, yes
'''


def can_remove(left_sign, right_sign, has_plus, has_minus):
    if (left_sign == '-' and has_minus
            or left_sign == '*' and has_plus
            or right_sign == '*' and has_plus
            or right_sign == '*' and has_minus
            or left_sign == '/' and has_plus
            or left_sign == '/' and has_minus
            or right_sign == '/' and has_plus
            or right_sign == '/' and has_minus):
        return False
    return True


def remove_parentheses(expression) -> str:
    ignore = set()  # set of indexes to ignore

    left_sign = [None] * len(expression)  # left sign of the expression
    right_sign = [None] * len(expression)  # right sign of the expression

    l = ''
    for i in range(len(expression)):
        left_sign[i] = l
        if expression[i] in ['+', '-', '*', '/']:
            l = expression[i]

    r = ''
    for i in range(len(expression)-1, -1, -1):
        right_sign[i] = r
        if expression[i] in ['+', '-', '*', '/']:
            r = expression[i]

    # print(left_sign)
    # print(right_sign)

    stack = []
    for i in range(len(expression)):
        if expression[i] == '(':
            stack.append(i)
        elif expression[i] == ')':
            l, r = stack.pop(), i

            has_plus, has_minus = [False] * 2
            for j in range(l + 1, r):
                if expression[j] == '+':
                    has_plus = True
                elif expression[j] == '-':
                    has_minus = True

            # can't remove parentheses cases
            # print(l, r, left_sign[l], right_sign[r], has_plus, has_minus)
            # print(can_remove(left_sign[l], right_sign[r], has_plus, has_minus))
            if (can_remove(left_sign[l], right_sign[r], has_plus, has_minus)):
                ignore.add(l)
                ignore.add(r)

    # print(expression)
    # print(sorted(ignore))
    res = ''
    for i in range(len(expression)):
        if i not in ignore:
            res += expression[i]
    return res


# Example usage
print(remove_parentheses("1*(2+(3*(4+5)))"))  # Output: "1*(2+3*(4+5))"
print(remove_parentheses("2 + (3 / -5)"))     # Output: "2 + 3 / -5"
print(remove_parentheses("x+(y+z)+(t+(v+w))"))  # Output: "x+y+z+t+v+w"
