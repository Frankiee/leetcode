# [Important]
# https://leetcode.com/problems/word-search/description/
# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution(object):
    def exist_neighbour(self, board, word, r, c, word_index, used_indices):
        if word_index >= len(word):
            return True

        if r > 0 and board[r - 1][c] == word[word_index] and (
                r - 1, c) not in used_indices:
            used_indices.add((r - 1, c))
            if self.exist_neighbour(
                    board, word, r - 1, c, word_index + 1, used_indices):
                return True
            used_indices.remove((r - 1, c))

        if c > 0 and board[r][c - 1] == word[word_index] and (
                r, c - 1) not in used_indices:
            used_indices.add((r, c - 1))
            if self.exist_neighbour(
                    board, word, r, c - 1, word_index + 1, used_indices):
                return True
            used_indices.remove((r, c - 1))

        if r < len(board) - 1 and board[r + 1][c] == word[word_index] and (
                r + 1, c) not in used_indices:
            used_indices.add((r + 1, c))
            if self.exist_neighbour(
                    board, word, r + 1, c, word_index + 1, used_indices):
                return True
            used_indices.remove((r + 1, c))

        if c < len(board[0]) - 1 and board[r][c + 1] == word[word_index] and (
                r, c + 1) not in used_indices:
            used_indices.add((r, c + 1))
            if self.exist_neighbour(
                    board, word, r, c + 1, word_index + 1, used_indices):
                return True
            used_indices.remove((r, c + 1))

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.exist_neighbour(board, word, r, c, 1, {(r, c)}):
                        return True

        return False
