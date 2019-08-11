# https://leetcode.com/problems/sliding-puzzle/
# 773. Sliding Puzzle

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

import copy


class Board(object):
    def __init__(self, board, empty_idx):
        self.board = board
        self.empty_idx = empty_idx

    def _deep_copy_board(self):
        board = copy.deepcopy(self.board)
        empty_idx = copy.deepcopy(self.empty_idx)

        return Board(board, empty_idx)

    def __hash__(self):
        ret = 0
        for c in self.board:
            ret = ret * 10 + c
        return ret

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def _move_lambda(
            self, seen, ret, empty_r, empty_c, new_empty_r, new_empty_c, move):
        new_board = self._deep_copy_board()
        zero_idx = empty_c + empty_r * 3
        new_board.board[zero_idx], new_board.board[move(zero_idx)] = (
            new_board.board[move(zero_idx)], new_board.board[zero_idx])
        new_board.empty_idx = (new_empty_r, new_empty_c)
        if new_board not in seen:
            seen.add(new_board)
            ret.append(new_board)

    def move_next(self, seen):
        ret = []
        empty_r, empty_c = self.empty_idx

        # up
        if empty_r == 1:
            self._move_lambda(
                seen, ret, empty_r, empty_c, empty_r - 1, empty_c,
                lambda idx: idx - 3
            )

        # down
        if empty_r == 0:
            self._move_lambda(
                seen, ret, empty_r, empty_c, empty_r + 1, empty_c,
                lambda idx: idx + 3
            )

        # left
        if empty_c > 0:
            self._move_lambda(
                seen, ret, empty_r, empty_c, empty_r, empty_c - 1,
                lambda idx: idx - 1
            )

        # right
        if empty_c < 2:
            self._move_lambda(
                seen, ret, empty_r, empty_c, empty_r, empty_c + 1,
                lambda idx: idx + 1
            )

        return ret


class Solution(object):
    def __init__(self):
        self.seen = set()
        self.current = []

    def _find_empty(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    return r, c

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = [1, 2, 3, 4, 5, 0]
        empty = self._find_empty(board)

        board_list = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                board_list.append(board[r][c])

        board = Board(board_list, empty)
        if goal == board.board:
            return 0

        self.current.append(board)
        self.seen.add(board)

        moves = 0
        while self.current:
            self.new_current = []
            for b in self.current:
                self.new_current.extend(b.move_next(self.seen))
            moves += 1

            if any([goal == b.board for b in self.new_current]):
                return moves

            self.current = self.new_current

        return -1
