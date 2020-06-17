# https://leetcode.com/problems/powx-n/
# 50. Pow(x, n)

# History:
# Facebook
# 1.
# Mar 29, 2020
# 2.
# May 4, 2020

# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        is_negative = False
        if n < 0:
            n = -n
            is_negative = True

        if n % 2 == 0:
            ret = self.myPow(x * x, n / 2)
        else:
            ret = x * self.myPow(x, n - 1)

        return ret if not is_negative else 1 / ret
