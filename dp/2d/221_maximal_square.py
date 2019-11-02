# [2D-DP]
# https://leetcode.com/problems/maximal-square/
# 221. Maximal Square

# History:
# 1.
# Nov 1, 2019
# Daily Interview Pro

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's
# and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        dp = [[None] * len(matrix[0]) for r in range(len(matrix))]
        max_len = float('-inf')

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                elif matrix[r][c] == '0':
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(
                        dp[r][c - 1],
                        dp[r - 1][c],
                        dp[r - 1][c - 1],
                    ) + 1

                max_len = max(max_len, dp[r][c])

        return max_len ** 2
