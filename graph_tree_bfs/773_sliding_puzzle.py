# https://leetcode.com/problems/sliding-puzzle/
# 773. Sliding Puzzle

# History:
# Google
# 1.
# Apr 29, 2019
# 2.
# Mar 17, 2020
# 3.
# May 8, 2020

# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,
# 5,0]].
#
# Given a puzzle board, return the least number of moves required so that
# the state of the board is solved. If it is impossible for the state of the
# board to be solved, return -1.
#
# Examples:
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
#
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
#
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# Note:
#
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].


class Solution(object):
    GOAL = '123450'

    def _encode_board(self, board):
        return "".join([str(c) for r in board for c in r])

    def _generate_moves(self, board):
        for i in range(len(board)):
            if board[i] == '0':
                break

        r = i / 3
        c = i - 3 * r

        ret = []
        for n_r, n_c in [(r + 1, c), [r - 1, c], [r, c + 1], [r, c - 1]]:
            if 0 <= n_r < 2 and 0 <= n_c < 3:
                nxt_i = 3 * n_r + n_c

                if nxt_i < i:
                    nxt_board = (
                        board[:nxt_i] + board[i] + board[nxt_i + 1:i] +
                        board[nxt_i] + board[i + 1:])
                else:
                    nxt_board = (
                        board[:i] + board[nxt_i] + board[i + 1:nxt_i] +
                        board[i] + board[nxt_i + 1:])

                ret.append(nxt_board)

        return ret

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        to_do = [self._encode_board(board)]
        visited = set(to_do)

        ret = 0
        while to_do:
            next_to_do = []

            for board in to_do:
                if board == self.GOAL:
                    return ret

                for move in self._generate_moves(board):
                    if move in visited:
                        continue

                    visited.add(move)
                    next_to_do.append(move)

            ret += 1
            to_do = next_to_do

        return -1
