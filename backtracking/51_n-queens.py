# [Important]
# https://leetcode.com/problems/n-queens/
# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n*n
# chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.


class Solution(object):
    def __init__(self):
        self.sum_occupy = set()
        self.diff_occupy = set()
        self.column_occupy = set()

    def can_take(self, r, c, n, prefix):
        return (
            (r + c) not in self.sum_occupy and
            (r - c) not in self.diff_occupy and
            c not in self.column_occupy
        )

    def take(self, r, c, prefix):
        self.sum_occupy.add(r + c)
        self.diff_occupy.add(r - c)
        self.column_occupy.add(c)
        prefix[r][c] = 'Q'

    def untake(self, r, c, prefix):
        self.sum_occupy.remove(r + c)
        self.diff_occupy.remove(r - c)
        self.column_occupy.remove(c)
        prefix[r][c] = '.'

    def solve_nqueens(self, ret, n, r, c, prefix):
        if r >= n:
            board = [''.join(r) for r in prefix]
            ret.append(board)
            return

        for c in range(n):
            if self.can_take(r, c, n, prefix):
                # take r, c
                self.take(r, c, prefix)
                self.solve_nqueens(ret, n, r + 1, 0, prefix)
                self.untake(r, c, prefix)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []

        prefix = []
        for r in range(n):
            prefix.append(["."] * n)
        self.solve_nqueens(ret, n, 0, 0, prefix)

        return ret
