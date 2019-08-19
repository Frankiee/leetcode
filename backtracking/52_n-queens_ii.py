# [Important]
# https://leetcode.com/problems/n-queens-ii/
# 52. N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n*n
# chessboard such that no two queens attack each other.
#
#
# Given an integer n, return the number of distinct solutions to the
# n-queens puzzle.
#
# Example:
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown below.
# [
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


class Solution(object):
    def __init__(self):
        self.sum_occupy = set()
        self.diff_occupy = set()
        self.column_occupy = set()

        self.ret = 0

    def can_take(self, r, c, n):
        return (
            (r + c) not in self.sum_occupy and
            (r - c) not in self.diff_occupy and
            c not in self.column_occupy
        )

    def take(self, r, c):
        self.sum_occupy.add(r + c)
        self.diff_occupy.add(r - c)
        self.column_occupy.add(c)

    def untake(self, r, c):
        self.sum_occupy.remove(r + c)
        self.diff_occupy.remove(r - c)
        self.column_occupy.remove(c)

    def solve_nqueens(self, n, r, c):
        if r >= n:
            self.ret += 1
            return

        for c in range(n):
            if self.can_take(r, c, n):
                # take r, c
                self.take(r, c)
                self.solve_nqueens(n, r + 1, 0)
                self.untake(r, c)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.solve_nqueens(n, 0, 0)

        return self.ret
