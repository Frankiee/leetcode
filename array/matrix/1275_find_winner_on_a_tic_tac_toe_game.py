# [Matrix]
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# 1275. Find Winner on a Tic Tac Toe Game

# History:
# 1.
# Sep 18, 2021

# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
#
# Here are the rules of Tic-Tac-Toe:
#
# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the
# grid where they mark their respective character in the order in which A and B play.
#
# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are
# still movements to play return "Pending".
#
# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A
# will play first.
#
#
#
# Example 1:
#
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: "A" wins, he always plays first.
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
# Example 2:
#
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: "B" wins.
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
# "   "    "   "    "   "    "   "    "   "    "O  "
# Example 3:
#
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# "XXO"
# "OOX"
# "XOX"
# Example 4:
#
# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
# "X  "
# " O "
# "   "
#
#
# Constraints:
#
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= moves[i][j] <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        rows = [0] * 3
        cols = [0] * 3
        diag = cdiag = 0

        for i, m in enumerate(moves):
            delta = 1 if i % 2 == 0 else -1
            rows[m[0]] += delta

            if rows[m[0]] in {3, -3}:
                return "A" if i % 2 == 0 else "B"

            cols[m[1]] += delta
            if cols[m[1]] in {3, -3}:
                return "A" if i % 2 == 0 else "B"

            if m in [[1, 1], [0, 0], [2, 2]]:
                diag += delta
            if m in [[1, 1], [0, 2], [2, 0]]:
                cdiag += delta
            if diag in {3, -3} or cdiag in {3, -3}:
                return "A" if i % 2 == 0 else "B"

        return "Pending" if len(moves) < 9 else "Draw"
