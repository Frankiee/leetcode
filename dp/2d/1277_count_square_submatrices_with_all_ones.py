# [2D-DP, Classic]
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# 1277. Count Square Submatrices with All Ones

# History:
# Google
# 1.
# Mar 9, 2020

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#
#
#
# Example 1:
#
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
#
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
#
#
# Constraints:
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        ret = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    curr_max_square = matrix[r][c]
                else:
                    curr_max_square = (
                        0 if matrix[r][c] == 0 else
                        1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    )
                dp[r][c] = curr_max_square
                ret += curr_max_square

        return ret
