# [Bisect-Lower-Bound]
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
# 1428. Leftmost Column with at Least a One

# History:
# Facebook
# 1.
# May 11, 2020

# (This problem is an interactive problem.)
#
# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
# this row is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at
# least a 1 in it. If such index doesn't exist, return -1.
#
# You can't access the Binary Matrix directly.  You may only access the matrix using a
# BinaryMatrix interface:
#
# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is
# rows * cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also,
# any solutions that attempt to circumvent the judge will result in disqualification.
#
# For custom testing purposes you're given the binary matrix mat as input in the following four
# examples. You will not have access the binary matrix directly.
#
#
#
#
#
#
#
# Example 1:
#
#
#
# Input: mat = [[0,0],[1,1]]
# Output: 0
# Example 2:
#
#
#
# Input: mat = [[0,0],[0,1]]
# Output: 1
# Example 3:
#
#
#
# Input: mat = [[0,0],[0,0]]
# Output: -1
# Example 4:
#
#
#
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
#
#
# Constraints:
#
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in a non-decreasing way.


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class SolutionFound(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row_count, col_count = binaryMatrix.dimensions()

        found = False
        col_to_check = col_count - 1

        for row in range(row_count):
            if binaryMatrix.get(row, col_to_check) == 0:
                continue

            l, r = 0, col_to_check + 1
            while l < r:
                m = (r - l) / 2 + l

                if binaryMatrix.get(row, m) == 1:
                    r = m
                else:
                    l = m + 1

            if l < col_count:
                if binaryMatrix.get(row, l) == 1:
                    found = True
                col_to_check = min(col_to_check, l)

        return col_to_check if found else -1


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class SolutionNoExists(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row_count, col_count = binaryMatrix.dimensions()

        curr_col_p_one = col_count
        for row in range(row_count):
            if curr_col_p_one == 0:
                return 0

            if binaryMatrix.get(row, curr_col_p_one - 1) == 0:
                continue

            l, r = 0, curr_col_p_one
            while l < r:
                m = (r - l) / 2 + l

                if binaryMatrix.get(row, m) == 1:
                    r = m
                else:
                    l = m + 1

            curr_col_p_one = l

        return curr_col_p_one if curr_col_p_one < col_count else -1
