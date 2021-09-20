# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# May 2, 2020
# 3.
# Jul 21, 2021

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your
# function returns 0 when the reversed integer overflows.


class Solution(object):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = - 2 ** 31

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
        ret = 0

        while x:
            ret *= 10
            ret += x % 10
            x /= 10

        ret = ret if not is_negative else -ret

        return ret if self.MIN_INT < ret < self.MAX_INT else 0
