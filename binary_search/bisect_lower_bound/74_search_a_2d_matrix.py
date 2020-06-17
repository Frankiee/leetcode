# [Bisect-Lower-Bound]
# https://leetcode.com/problems/search-a-2d-matrix/
# 74. Search a 2D Matrix

# History:
# Facebook
# 1.
# Aug 18, 2019
# 2.
# Mar 8, 2020
# 3.
# May 12, 2020

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


class SolutionBinarySearch1(object):
    def _get_row(self, matrix, target):
        l, r = 0, len(matrix)

        while l < r:
            m = (r - l) / 2 + l

            if matrix[m][-1] >= target:
                r = m
            else:
                l = m + 1

        return l

    def _bisect_lower(self, row, target):
        l, r = 0, len(row)

        while l < r:
            m = (r - l) / 2 + l

            if row[m] >= target:
                r = m
            else:
                l = m + 1

        return l

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row = self._get_row(matrix, target)

        if row == len(matrix):
            return False

        pos = self._bisect_lower(matrix[row], target)

        return pos < len(matrix[row]) and matrix[row][pos] == target


class SolutionBinarySearch2(object):
    def _bisect(self, lst, target, key_fn):
        l, r = 0, len(lst)

        while l < r:
            m = (r - l) / 2 + l

            if key_fn(lst[m]) >= target:
                r = m
            else:
                l = m + 1

        return l

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row_idx = self._bisect(matrix, target, key_fn=lambda row: row[0])
        if row_idx < len(matrix) and matrix[row_idx][0] == target:
            return True
        if row_idx == 0:
            return False

        col_idx = self._bisect(matrix[row_idx - 1], target, key_fn=lambda ele: ele)

        return 0 <= col_idx < len(matrix[0]) and matrix[row_idx - 1][col_idx] == target


class SolutionDeprecated(object):
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
