# https://leetcode.com/problems/factorial-trailing-zeroes/
# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0

        i = 5
        while n / i > 0:
            ret += n / i
            i *= 5

        return ret