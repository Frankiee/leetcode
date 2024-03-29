# [Classic, DP-Sequence-Action]
# https://leetcode.com/problems/domino-and-tromino-tiling/
# 790. Domino and Tromino Tiling

# https://www.youtube.com/watch?v=S-fUTfqrdq8

# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
#
# XX  <- domino
#
# XX  <- "L" tromino
# X
# Given N, how many ways are there to tile a 2 x N board? Return your answer
# modulo 10^9 + 7.
#
# (In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on
# the board such that exactly one of the tilings has both squares occupied
# by a tile.)
#
# Example:
# Input: 3
# Output: 5
# Explanation:
# The five different ways are listed below, different letters indicates
# different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# Note:
#
# N  will be in range [1, 1000].


class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[0] * 2 for i in range(N + 1)]

        # the column will end
        # 0: in flat
        # 1: with bottom/top stick out

        for i in range(1, N + 1):
            if i == 1:
                dp[i][0] = 1
                dp[i][1] = 1
            elif i == 2:
                dp[i][0] = 2
                dp[i][1] = 2
            else:
                dp[i][0] = (
                    dp[i - 1][0] +
                    dp[i - 2][0] +
                    dp[i - 2][1] * 2
                ) % mod
                dp[i][1] = (
                    dp[i - 1][0] +
                    dp[i - 1][1]
                ) % mod

        return dp[-1][0]
