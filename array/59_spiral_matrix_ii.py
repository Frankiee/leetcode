# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


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

    def can_write(self, matrix, n, r, c):
        if r < 0 or r > n - 1:
            return False
        if c < 0 or c > n - 1:
            return False
        if matrix[r][c]:
            return False
        return True

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        for r in range(n):
            ret.append([None] * n)

        c_r = c_c = 0
        for i in range(1, n ** 2 + 1):
            ret[c_r][c_c] = i
            n_r, n_c = self.get_next_position(c_r, c_c)
            if not self.can_write(ret, n, n_r, n_c):
                self.direction = (self.direction + 1) % 4
                n_r, n_c = self.get_next_position(c_r, c_c)
            c_r, c_c = n_r, n_c

        return ret
