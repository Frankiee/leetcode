# [Classic]
# https://leetcode.com/problems/word-search-ii/
# 212. Word Search II

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# May 15, 2020

# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used
# more than once in a word.
#
#
#
# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
# Note:
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class Solution1(object):
    def __init__(self):
        self.trie_root = TrieNode()

    def _add_word(self, w):
        self.curr = self.trie_root

        for c in w:
            if c not in self.curr.children:
                self.curr.children[c] = TrieNode()
            self.curr = self.curr.children[c]

        self.curr.is_terminal = True

    def _dfs(self, r, c, board, trie_node, ret, curr):
        if trie_node.is_terminal:
            ret.append(curr)
            trie_node.is_terminal = False

        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return

        nxt_char = board[r][c]
        if nxt_char not in trie_node.children:
            return

        board[r][c] = '#'

        for n_r, n_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
            self._dfs(n_r, n_c, board, trie_node.children[nxt_char], ret, curr + nxt_char)

        board[r][c] = nxt_char

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for w in words:
            self._add_word(w)

        ret = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self._dfs(r, c, board, self.trie_root, ret, "")

        return ret


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class Solution2(object):
    def __init__(self):
        self.trie_root = TrieNode()

    def _add_words(self, word):
        curr = self.trie_root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.is_terminal = True

    def _dfs(self, board, trie, r, c, curr):
        if trie.is_terminal:
            self.ret.append(curr)
            trie.is_terminal = False
            return

        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] in trie.children:
            nxt_char = board[r][c]
            board[r][c] = '#'

            for n_r, n_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                self._dfs(board, trie.children[nxt_char], n_r, n_c, curr + nxt_char)

            board[r][c] = nxt_char

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for word in words:
            self._add_words(word)

        self.ret = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self._dfs(board, self.trie_root, r, c, "")

        return self.ret
