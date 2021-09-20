# [Archived]
# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number

# History:
# Facebook
# 1.
# Mar 6, 2020
# 2.
# Apr 30, 2020
# 3.
# July 26, 2021

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
#
#
#1245
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
# Note:
#
# 0 ≤ N ≤ 30.


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1

        i_m_1, i_m_2 = 1, 0
        for i in range(2, N + 1):
            i_m_1, i_m_2 = i_m_1 + i_m_2, i_m_1

        return i_m_1
