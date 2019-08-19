# [Important]
# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements
# of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def __init__(self):
        # 0: right
        # 1: down
        # 2: left
        # 3: up
        self.direction = 0

    def get_next_position(self, r, c):
        if self.direction == 0:
            return r, c + 1
        elif self.direction == 1:
            return r + 1, c
        elif self.direction == 2:
            return r, c - 1
        else:
            return r - 1, c

    def can_read(self, matrix, r, c):
        if r < 0 or r >= len(matrix):
            return False
        if c < 0 or c >= len(matrix[r]):
            return False
        if matrix[r][c] is not None:
            return True
        return False

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if not matrix:
            return ret

        c_r = c_c = 0
        while True:
            ret.append(matrix[c_r][c_c])
            matrix[c_r][c_c] = None
            n_r, n_c = self.get_next_position(c_r, c_c)
            if not self.can_read(matrix, n_r, n_c):
                self.direction = (self.direction + 1) % 4
                n_r, n_c = self.get_next_position(c_r, c_c)
                if not self.can_read(matrix, n_r, n_c):
                    return ret
            c_r, c_c = n_r, n_c
