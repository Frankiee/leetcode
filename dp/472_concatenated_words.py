# https://leetcode.com/problems/concatenated-words/
# 472. Concatenated Words

# History:
# Facebook
# 1.
# May 12, 2020

# Given a list of words (without duplicates), please write a program that returns all
# concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter
# words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.


class Solution(object):
    def _check_concatenated(self, dictionary, word):
        dp = [False] * (len(word) + 1)

        for r in range(len(word) + 1):
            for l in range(r):
                if (l == 0 or dp[l]) and word[l:r] in dictionary:
                    dp[r] = True
                    break

        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = sorted(words, key=lambda w: len(w))
        dictionary = set()

        ret = []
        for w in words:
            if self._check_concatenated(dictionary, w):
                ret.append(w)

            dictionary.add(w)

        return ret
