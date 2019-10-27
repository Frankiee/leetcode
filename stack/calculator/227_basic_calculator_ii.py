# [Calculator, Google, Classic]
# https://leetcode.com/problems/basic-calculator-ii/
# 227. Basic Calculator II

# History:
# 1.
# Oct 20, 2019
# Daily Interview Pro - Google

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *,
# / operators and empty spaces . The integer division should truncate toward
# zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5
# Note:
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        num = 0
        pre_sign = "+"

        # make sure last number also got calculated
        s += '+'

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                num = num * 10 + int(c)
                continue

            if pre_sign == '+':
                stack.append(num)
            elif pre_sign == '-':
                stack.append(-num)
            elif pre_sign == '*':
                stack.append(num * stack.pop())
            elif pre_sign == '/':
                stack_num = stack.pop()

                if stack_num >= 0:
                    stack.append(stack_num / num)
                else:
                    stack.append(-(-stack_num / num))

            num = 0
            pre_sign = c

        return sum(stack)
