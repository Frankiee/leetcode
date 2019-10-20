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

        number = 0
        sign = '+'

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                number = number * 10 + int(c)

            if (c != ' ' and not c.isdigit()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack.append(number * stack.pop())
                elif sign == '/':
                    # Truncate towards 0
                    div = stack.pop() / float(number)
                    if div > 0:
                        div = int(div)
                    else:
                        div = -int(-div)

                    stack.append(div)

                number = 0
                sign = c

        return sum(stack)
