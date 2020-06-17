# https://leetcode.com/problems/set-matrix-zeroes/
# 73. Set Matrix Zeroes

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 22, 2020

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col0 = 1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0

                    if c == 0:
                        col0 = 0
                    else:
                        matrix[0][c] = 0

        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[0]) - 1, -1, -1):
                if matrix[r][0] == 0 or (matrix[0][c] == 0 if c != 0 else col0 == 0):
                    matrix[r][c] = 0


class SolutionTwoVariable(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix

        first_row_zero = False
        first_column_zero = False

        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_column_zero = True
                break

        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0

        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[0]) - 1, -1, -1):
                if r == 0:
                    if first_row_zero:
                        matrix[r][c] = 0
                if c == 0:
                    if first_column_zero:
                        matrix[r][c] = 0

                if r != 0 and c != 0 and matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
