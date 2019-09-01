# [Archived]
# https://leetcode.com/problems/alphabet-board-path/
# 1138. Alphabet Board Path

# On an alphabet board, we start at position (0, 0), corresponding to
# character board[0][0].
#
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown
# in the diagram below.
#
#
# We may make the following moves:
#
# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the
# answer.
# (Here, the only positions that exist on the board are positions with
# letters on them.)
#
# Return a sequence of moves that makes our answer equal to target in the
# minimum number of moves.  You may return any path that does so.
#
#
#
# Example 1:
#
# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# Example 2:
#
# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"
#
#
# Constraints:
#
# 1 <= target.length <= 100
# target consists only of English lowercase letters.


class Solution(object):
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    position = dict([
        (board[r][c], (r, c))
        for r in range(len(board))
        for c in range(len(board[r]))
    ])

    def punch_next(self, current_r, current_c, char, ret):
        to_r, to_c = self.position[char]

        while current_r != to_r or current_c != to_c:
            while (to_r > current_r and
                   0 <= current_r + 1 < len(self.board) and
                   0 <= current_c < len(self.board[current_r + 1])):
                ret += 'D'
                current_r += 1
            while (to_r < current_r and
                   0 <= current_r - 1 < len(self.board) and
                   0 <= current_c < len(self.board[current_r - 1])):
                ret += 'U'
                current_r -= 1
            while (to_c > current_c and
                   0 <= current_r < len(self.board) and
                   0 <= current_c + 1 < len(self.board[current_r])):
                ret += 'R'
                current_c += 1
            while (to_c < current_c and
                   0 <= current_r < len(self.board) and
                   0 <= current_c - 1 < len(self.board[current_r])):
                ret += 'L'
                current_c -= 1
        ret += '!'

        return to_r, to_c, ret

    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        ret = ""

        current_r = current_c = 0

        for c in target:
            current_r, current_c, ret = self.punch_next(
                current_r, current_c, c, ret,
            )

        return ret
