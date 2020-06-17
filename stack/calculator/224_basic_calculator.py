# [Calculator, Classic]
# https://leetcode.com/problems/basic-calculator/
# 224. Basic Calculator

# History:
# Google
# 1.
# Oct 20, 2019
# 2.
# Feb 9, 2020
# 3.
# Apr 26, 2020
# 4.
# May 3, 2020

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

        ret = 0

        sign = 1
        num = 0

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                ret += sign * num

                sign = 1
                num = 0
            elif c == '-':
                ret += sign * num

                sign = -1
                num = 0
            elif c == '(':
                stack.append(sign)
                stack.append(ret)

                sign = 1
                num = 0
                ret = 0
            elif c == ')':
                ret += sign * num

                pre_ret = stack.pop()
                pre_sign = stack.pop()

                ret = pre_ret + pre_sign * ret

                sign = 1
                num = 0

        if num:
            ret += sign * num

        return ret


class SolutionPushAllStack(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = 1
        curr_num = 0

        s += '+'

        for c in s:
            if c.isdigit():
                curr_num *= 10
                curr_num += int(c)
            elif c in {'+', '-'}:
                stack.append(sign * curr_num)
                curr_num = 0
                sign = 1

                if c == '-':
                    sign = -1
            elif c == '(':
                stack.append(sign)
                stack.append('(')

                curr_num = 0
                sign = 1
            elif c == ')':
                stack.append(sign * curr_num)
                curr_num = 0
                sign = 1

                total = 0
                while stack and stack[-1] != '(':
                    total += stack.pop(-1)

                stack.pop()
                stack.append(stack.pop() * total)

        return sum(stack)
