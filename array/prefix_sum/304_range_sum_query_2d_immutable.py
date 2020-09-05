# [Prefix-Sum]
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# 304. Range Sum Query 2D - Immutable

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# Apr 9, 2020
# 3.
# May 12, 2020
# 4.
# July 30, 2020

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its
# upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2,
# col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.rolling_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 and c == 0:
                    self.rolling_sum[r][c] = matrix[r][c]
                elif r == 0:
                    self.rolling_sum[r][c] = self.rolling_sum[r][c - 1] + matrix[r][c]
                elif c == 0:
                    self.rolling_sum[r][c] = self.rolling_sum[r - 1][c] + matrix[r][c]
                else:
                    self.rolling_sum[r][c] = self.rolling_sum[r][c - 1] + self.rolling_sum[r - 1][
                        c] - self.rolling_sum[r - 1][c - 1] + matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.rolling_sum[row2][col2]

        if row1 >= 1:
            ret -= self.rolling_sum[row1 - 1][col2]
        if col1 >= 1:
            ret -= self.rolling_sum[row2][col1 - 1]
        if row1 >= 1 and col1 >= 1:
            ret += self.rolling_sum[row1 - 1][col1 - 1]

        return ret

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
