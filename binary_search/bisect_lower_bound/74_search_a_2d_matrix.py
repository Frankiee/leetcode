# [Bisect-Lower-Bound]
# https://leetcode.com/problems/search-a-2d-matrix/
# 74. Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# Example 1:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


class Solution(object):
    def bisect(self, matrix, target, key=None):
        l = 0
        r = len(matrix)

        while l < r:
            m = l + (r - l) / 2

            num = key(matrix[m]) if key else matrix[m]
            if num < target:
                l = m + 1
            elif num == target:
                return m
            else:
                r = m

        return l

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row_bisect = self.bisect(matrix, target, key=lambda r: r[-1])
        if row_bisect >= len(matrix):
            return False
        if matrix[row_bisect] == target:
            return True
        column_bisect = self.bisect(matrix[row_bisect], target)
        if column_bisect >= len(matrix[0]):
            return False
        if matrix[row_bisect][column_bisect] == target:
            return True

        return False
