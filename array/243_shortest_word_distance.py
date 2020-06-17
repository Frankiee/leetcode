# https://leetcode.com/problems/shortest-word-distance/
# 243. Shortest Word Distance

# History:
# LinkedIn
# 1.
# Mar 25, 2020

# Given a list of words and two words word1 and word2, return the shortest distance between these
# two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_last_idx, word2_last_idx = float('-inf'), float('-inf')

        ret = float('inf')
        for idx, word in enumerate(words):
            if word == word1:
                word1_last_idx = idx
                ret = min(ret, word1_last_idx - word2_last_idx)
            elif word == word2:
                word2_last_idx = idx
                ret = min(ret, word2_last_idx - word1_last_idx)

        return ret
