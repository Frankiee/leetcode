# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all
# regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn't be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.


class Solution(object):
    def _mark_edge(self, board, r, c):
        if (0 <= r < len(board) and 0 <= c < len(board[0]) and
                board[r][c] == 'O'):
            board[r][c] = 'E'
            self._mark_edge(board, r, c + 1)
            self._mark_edge(board, r, c - 1)
            self._mark_edge(board, r + 1, c)
            self._mark_edge(board, r - 1, c)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        for c in range(len(board[0])):
            # Top
            if board[0][c] == 'O':
                self._mark_edge(board, 0, c)
            # Bottom
            if board[len(board) - 1][c] == 'O':
                self._mark_edge(board, len(board) - 1, c)

        for r in range(1, len(board) - 1):
            # Left
            if board[r][0] == 'O':
                self._mark_edge(board, r, 0)
            if board[r][len(board[0]) - 1]:
                self._mark_edge(board, r, len(board[0]) - 1)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
