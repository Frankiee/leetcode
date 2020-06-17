# [Classic]
# https://leetcode.com/problems/number-of-matching-subsequences/
# 792. Number of Matching Subsequences

# Related:
# 392. Is Subsequence

# History:
# TikTok
# 1.
# Aug 12, 2019
# 2.
# Nov 23, 2019

# Given string S and a dictionary of words words, f ind the number of words[
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

        for c in S:
            if c in waiting:
                waiting_words = waiting.pop(c)

                for w in waiting_words:
                    if len(w) > 0:
                        waiting[w[0]].append(w[1:])

        return len(words) - sum([len(ws) for ws in waiting.values()])
