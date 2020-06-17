# [Classic]
# https://leetcode.com/problems/word-ladder/
# 127. Word Ladder

# History:
# Facebook
# 1.
# Mar 1, 2020
# 2.
# Apr 24, 2020

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of
# shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


class Solution(object):
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'

    def _get_neighbours(self, curr_word, wordList):
        ret = []

        for i in range(len(curr_word)):
            for c in self.ALPHA:
                new_w = curr_word[:i] + c + curr_word[i + 1:]
                if new_w in wordList:
                    ret.append(new_w)
                    wordList.remove(new_w)

        return ret

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        to_do = [beginWord]

        ret = 1
        while to_do:
            nxt_to_do = []

            for w in to_do:
                if w == endWord:
                    return ret

                neighbours = self._get_neighbours(w, wordList)
                nxt_to_do.extend(neighbours)

            ret += 1

            to_do = nxt_to_do

        return 0
