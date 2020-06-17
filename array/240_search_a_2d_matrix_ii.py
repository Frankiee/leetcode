# [Classic]
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# 240. Search a 2D Matrix II

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 3, 2020
# 3.
# Apr 25, 2020

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the
# following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        r, c = 0, len(matrix[0]) - 1

        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False
