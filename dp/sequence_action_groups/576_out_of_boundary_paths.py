# [DP-Sequence-Action-Groups, Classic]
# https://leetcode.com/problems/out-of-boundary-paths/
# 576. Out of Boundary Paths

# There is an m by n grid with a ball. Given the start coordinate (i,
# j) of the ball, you can move the ball to adjacent cell or cross the grid
# boundary in four directions (up, down, left, right). However, you can at
# most move N times. Find out the number of paths to move the ball out of
# grid boundary. The answer may be very large, return it after mod 109 + 7.
#
#
# Example 1:
#
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
#
# Example 2:
#
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
#
#
# Note:
#
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0:
            return 0

        dp = [None] * m
        for r in range(m):
            dp[r] = [[0, 0] for c in range(n)]
        current_idx, pre_idx = 0, 1

        # top & bottem
        for c in range(n):
            dp[0][c][current_idx] += 1
            dp[m - 1][c][current_idx] += 1

        # left, right
        for r in range(m):
            dp[r][0][current_idx] += 1
            dp[r][n - 1][current_idx] += 1

        ret = dp[i][j][current_idx]
        if N == 1:
            return ret

        divider = 10 ** 9 + 7

        for step in range(1, N):
            current_idx, pre_idx = pre_idx, current_idx

            for r in range(m):
                for c in range(n):
                    dp[r][c][current_idx] = 0
                    # from up
                    if r > 0:
                        dp[r][c][current_idx] += dp[r - 1][c][pre_idx]
                    # from down
                    if r < m - 1:
                        dp[r][c][current_idx] += dp[r + 1][c][pre_idx]
                    # from left
                    if c > 0:
                        dp[r][c][current_idx] += dp[r][c - 1][pre_idx]
                    # from right
                    if c < n - 1:
                        dp[r][c][current_idx] += dp[r][c + 1][pre_idx]
                    dp[r][c][current_idx] %= divider

            ret += dp[i][j][current_idx]
            ret %= divider

        return ret
