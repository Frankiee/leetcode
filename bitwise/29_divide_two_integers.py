# https://leetcode.com/problems/divide-two-integers/
# 29. Divide Two Integers

# History:
# Facebook
# 1.
# Mar 16, 2019
# 2.
# Feb 02, 2020
# 3.
# Apr 13, 2020
# 4.
# Apr 22, 2020

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
    MAX_INT = 2 ** 31 - 1
    MIN_INT = - 2 ** 31

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_negative = (
            dividend < 0 and divisor > 0 or
            dividend > 0 and divisor < 0
        )

        dividend, divisor = abs(dividend), abs(divisor)

        ret = 0
        for i in range(31, -1, -1):
            n = divisor << i
            if n <= dividend:
                ret += 1 << i
                dividend -= n

        return min(max(ret if not is_negative else -ret, self.MIN_INT), self.MAX_INT)


class SolutionBinarySearch(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # if divisor == 1:
        #     return dividend
        # elif divisor == -1:
        #     return -dividend
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_negative = (
            dividend > 0 and divisor < 0 or
            dividend < 0 and divisor > 0)

        dividend, divisor = abs(dividend), abs(divisor)

        l, r = 0, dividend + 1

        while l < r:
            m = (r - l) / 2 + l
            if m * divisor > dividend:
                r = m
            else:
                l = m + 1

        l -= 1
        return l if not is_negative else -l


class DeprecatedSolution(object):
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
