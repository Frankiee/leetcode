# [2D-DP]
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# 562. Longest Line of Consecutive One in Matrix

# History:
# Google
# 1.
# Mar 26, 2020

# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be
# horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0

        # horizontal, vertical, diagonal or anti-diagonal
        dp = [[[0] * 4 for _ in range(len(M[0]))] for _ in range(len(M))]

        ret = 0
        for r in range(len(M)):
            for c in range(len(M[0])):
                if M[r][c] == 1:
                    if c == 0:
                        dp[r][c][0] = 1
                    else:
                        dp[r][c][0] = dp[r][c - 1][0] + 1

                    if r == 0:
                        dp[r][c][1] = 1
                    else:
                        dp[r][c][1] = dp[r - 1][c][1] + 1

                    if r > 0 and c > 0:
                        dp[r][c][2] = dp[r - 1][c - 1][2] + 1
                    else:
                        dp[r][c][2] = 1

                    if r > 0 and c < len(M[0]) - 1:
                        dp[r][c][3] = dp[r - 1][c + 1][3] + 1
                    else:
                        dp[r][c][3] = 1

                ret = max(ret, dp[r][c][0], dp[r][c][1], dp[r][c][2], dp[r][c][3])

        return ret
