# [Calculator, Google, Classic]
# https://leetcode.com/problems/basic-calculator/
# 224. Basic Calculator

# History:
# 1.
# Oct 20, 2019
# Daily Interview Pro - Google

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        number = 0
        result = 0
        pre_sign = 1

        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                result += pre_sign * number

                pre_sign = 1
                number = 0
            elif c == '-':
                result += pre_sign * number

                pre_sign = -1
                number = 0
            elif c == '(':
                stack.append(result)
                stack.append(pre_sign)

                pre_sign = 1
                number = 0
                result = 0
            elif c == ')':
                result += pre_sign * number

                pre_sign = 1
                number = 0

                result *= stack.pop()
                result += stack.pop()

        result += pre_sign * number
        return result
