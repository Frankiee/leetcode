# [Matrix]
# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II

# History:
# TikTok
# 1.
# Aug 18, 2020
# 2.
# Apr 26, 2020

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


class SolutionLengthMinusOne1(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        r, c = 0, -1
        horizontal_length, vertical_length = n, n - 1
        horizontal_incre = vertical_incre = True

        is_horizontal = True

        ret = [[None] * n for _ in range(n)]

        curr_i = 1
        while horizontal_length > 0 or vertical_length > 0:
            if is_horizontal:
                if horizontal_incre:
                    for c in range(c + 1, c + 1 + horizontal_length):
                        ret[r][c] = curr_i
                        curr_i += 1
                else:
                    for c in range(c - 1, c - 1 - horizontal_length, -1):
                        ret[r][c] = curr_i
                        curr_i += 1
                horizontal_incre = not horizontal_incre
                horizontal_length -= 1
            else:
                if vertical_incre:
                    for r in range(r + 1, r + 1 + vertical_length):
                        ret[r][c] = curr_i
                        curr_i += 1
                else:
                    for r in range(r - 1, r - 1 - vertical_length, -1):
                        ret[r][c] = curr_i
                        curr_i += 1
                vertical_incre = not vertical_incre
                vertical_length -= 1

            is_horizontal = not is_horizontal

        return ret


class SolutionLengthMinusOne2(object):
    SIDE_UP = 1
    SIDE_RIGHT = 2
    SIDE_DOWN = 3
    SIDE_LEFT = 4

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        horizontal_n = n
        vertical_n = n - 1

        side = self.SIDE_UP

        r, c = 0, -1

        i = 1
        ret = [[None] * n for _ in range(n)]
        current_n = horizontal_n
        while current_n > 0:
            if side == self.SIDE_UP:
                for _ in range(current_n):
                    c += 1
                    ret[r][c] = i
                    i += 1
                side = self.SIDE_RIGHT
                horizontal_n -= 1
                current_n = vertical_n
            elif side == self.SIDE_RIGHT:
                for _ in range(current_n):
                    r += 1
                    ret[r][c] = i
                    i += 1
                side = self.SIDE_DOWN
                vertical_n -= 1
                current_n = horizontal_n
            elif side == self.SIDE_DOWN:
                for _ in range(current_n):
                    c -= 1
                    ret[r][c] = i
                    i += 1
                side = self.SIDE_LEFT
                horizontal_n -= 1
                current_n = vertical_n
            else:
                for _ in range(current_n):
                    r -= 1
                    ret[r][c] = i
                    i += 1
                side = self.SIDE_UP
                vertical_n -= 1
                current_n = horizontal_n

        return ret


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
