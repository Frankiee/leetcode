# [Classic]
# https://leetcode.com/problems/word-squares/
# 425. Word Squares

# History:
# Facebook
# 1.
# Mar 22, 2020

# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same
# string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each
# word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of
# words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of
# words in each word square matters).


from collections import defaultdict


class Solution(object):
    def _dfs(self, c_idx, words, prefixes, curr_words, ret):
        if c_idx == len(words[0]):
            ret.append(curr_words)
            return

        for w in prefixes.get("".join(curr_word[c_idx] for curr_word in curr_words), []):
            self._dfs(c_idx + 1, words, prefixes, curr_words + [w], ret)

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        prefixes = defaultdict(set)

        for i in range(1, len(words[0])):
            for w in words:
                prefixes[w[:i]].add(w)

        ret = []
        for w in words:
            self._dfs(1, words, prefixes, [w], ret)

        return ret
