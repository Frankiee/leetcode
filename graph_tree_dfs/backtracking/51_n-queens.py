# [Backtracking]
# https://leetcode.com/problems/n-queens/
# 51. N-Queens

# History:
# Facebook
# 1.
# May 15, 2020

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
        self.cols = set()
        self.sums = set()
        self.diff = set()

    def _can_take(self, r, c):
        return (
            c not in self.cols and
            (r + c) not in self.sums and
            (r - c) not in self.diff
        )

    def _take(self, r, c):
        self.cols.add(c)
        self.sums.add(r + c)
        self.diff.add(r - c)

    def _untake(self, r, c):
        self.cols.remove(c)
        self.sums.remove(r + c)
        self.diff.remove(r - c)

    def _solve_n_queens(self, n, r, curr, ret):
        if r == n:
            ret.append(["".join(i) for i in curr])
            return ret

        for c in range(n):
            if self._can_take(r, c):
                self._take(r, c)
                curr[r][c] = 'Q'
                self._solve_n_queens(n, r + 1, curr, ret)
                self._untake(r, c)
                curr[r][c] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        curr = [['.'] * n for _ in range(n)]
        self._solve_n_queens(n, 0, curr, ret)

        return ret
