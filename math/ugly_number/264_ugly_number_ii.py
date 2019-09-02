# [Prime-Factor, Ugly-Number]
# https://leetcode.com/problems/ugly-number-ii/
# 264. Ugly Number II

# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first
# 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.


class Solution(object):
    COMMON = (2 * 3 * 5) ** 32

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        current_nth = 0
        current_number = 1
        while True:
            if self.COMMON % current_number == 0:
                current_nth += 1
                if current_nth == n:
                    return current_number
            current_number += 1
