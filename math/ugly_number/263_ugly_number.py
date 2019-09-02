# [Prime-Factor, Ugly-Number]
# https://leetcode.com/problems/ugly-number/
# 263. Ugly Number

# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
# Input: 6
# Output: true
# Explanation: 6 = 2 * 3
# Example 2:
#
# Input: 8
# Output: true
# Explanation: 8 = 2 * 2 * 2
# Example 3:
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
# Note:
#
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [-231,  231 - 1].


# Optimal
class Solution1(object):
    COMMON = (2*3*5) ** 32

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and self.COMMON % num == 0


# Sub-optimal
class Solution2(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i

        return num == 1
