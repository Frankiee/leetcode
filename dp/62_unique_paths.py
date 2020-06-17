# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# History:
# 1.
# Oct 27, 2019
# Daily Interview Pro
# 2.
# Nov 29, 2019
# 3.
# Apr 28, 2020

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        current_dp = [None] * m
        previous_dp = [None] * m

        for r in range(n):
            for c in range(m):
                if r == 0 or c == 0:
                    current_dp[c] = 1
                else:
                    current_dp[c] = current_dp[c - 1] + previous_dp[c]

            current_dp, previous_dp = previous_dp, current_dp

        return previous_dp[-1]
