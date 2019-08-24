# https://leetcode.com/problems/number-of-matching-subsequences/
# 792. Number of Matching Subsequences

# Given string S and a dictionary of words words, find the number of words[
# i] that is a subsequence of S.
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S:
# "a", "acd", "ace".
# Note:
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].

from collections import defaultdict


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = defaultdict(list)

        for w in words:
            waiting[w[0]].append(w[1:])

        for s in S:
            waiting_words = waiting.get(s)
            if waiting_words:
                waiting_words = waiting.pop(s)

                for w in waiting_words:
                    if w:
                        waiting[w[0]].append(w[1:])

        return len(words) - sum(len(ws) for ws in waiting.values())
