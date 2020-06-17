# [2D-DP]
# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum

# History:
# Apple, Facebook
# 1.
# Mar 21, 2020
# 2.
# Apr 24, 2020

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return None

        dp = [[None] * len(grid[0]) for _ in range(len(grid))]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]

        return dp[-1][-1]
