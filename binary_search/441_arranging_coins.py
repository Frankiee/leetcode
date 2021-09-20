# https://leetcode.com/problems/arranging-coins/
# 441. Arranging Coins

# History:
# 1.
# Apr 11, 2021

# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.
#
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:
#
#
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
#
#
# Constraints:
#
# 1 <= n <= 231 - 1

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n

        while l < r:
            m = (r - l) / 2 + l

            m_level_full = (1 + m + 1) * (m + 1) / 2

            if m_level_full == n:
                return m + 1
            elif m_level_full > n:
                r = m
            else:
                l = m + 1

        return l
