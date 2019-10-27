# [Backtracking]
# https://leetcode.com/problems/word-search/description/
# 79. Word Search

# History:
# 1.
# Feb 13, 2019
# 2.
# Oct 27, 2019
# Daily Interview Pro

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
    def dfs(self, board, word, word_idx, b_r, b_c, visited):
        if word_idx >= len(word):
            return True

        for r, c in [(b_r + 1, b_c), (b_r - 1, b_c), (b_r, b_c + 1), (b_r, b_c - 1)]:
            if ((r, c) not in visited and
                    len(board) > r >= 0 and
                    len(board[0]) > c >= 0 and
                    word[word_idx] == board[r][c]):
                visited.add((r, c))
                if self.dfs(board, word, word_idx + 1, r, c, visited):
                    return True
                visited.remove((r, c))

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
                if board[r][c] == word[0] and self.dfs(board, word, 1, r, c, {(r, c)}):
                    return True

        return False
