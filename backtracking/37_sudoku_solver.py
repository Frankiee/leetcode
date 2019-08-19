# [Important]
# https://leetcode.com/problems/sudoku-solver/
# 37. Sudoku Solver

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.


class Solution(object):
    GRID_COUNT = 9

    def get_options(self, board, r, c):
        occured_num = [False] * self.GRID_COUNT

        for i in range(self.GRID_COUNT):
            if board[r][i] != '.':
                occured_num[int(board[r][i]) - 1] = True
        for i in range(self.GRID_COUNT):
            if board[i][c] != '.':
                occured_num[int(board[i][c]) - 1] = True
        for add_r in range(3):
            for add_c in range(3):
                new_r = r - r % 3 + add_r
                new_c = c - c % 3 + add_c
                if board[new_r][new_c] != '.':
                    occured_num[int(board[new_r][new_c]) - 1] = True

        ret = []

        for i in range(self.GRID_COUNT):
            if occured_num[i] == False:
                ret.append(i + 1)

        return ret

    def solve_sudoku(self, board, r, c):
        if r >= self.GRID_COUNT:
            return True

        next_r = r + 1 if c == self.GRID_COUNT - 1 else r
        next_c = c + 1 if c < self.GRID_COUNT - 1 else 0

        if board[r][c] != '.':
            return self.solve_sudoku(board, next_r, next_c)
        else:
            available_nums = self.get_options(board, r, c)
            for n in available_nums:
                board[r][c] = str(n)
                if self.solve_sudoku(board, next_r, next_c):
                    return True
            board[r][c] = '.'
            return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        return self.solve_sudoku(board, 0, 0)
