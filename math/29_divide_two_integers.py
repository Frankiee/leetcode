# https://leetcode.com/problems/divide-two-integers/
# 29. Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [-231,  231 - 1]. For the purpose
# of this problem, assume that your function returns 231 - 1 when the division
# result overflows.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        ret = 0

        while dividend >= divisor:
            real_divisor, i = divisor, 1

            while dividend >= real_divisor:
                dividend -= real_divisor
                ret += i
                i *= 2
                real_divisor *= 2

        ret = ret if is_positive else -ret

        return min(max(-2147483648, ret), 2147483647)
