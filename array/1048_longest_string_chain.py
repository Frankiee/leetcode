# https://leetcode.com/problems/longest-string-chain/
# 1048. Longest String Chain

# History:
# Google
# 1.
# Mar 14, 2020

# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere
# in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is
# a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.
#
#
#
# Example 1:
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
# Note:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mp = defaultdict(set)
        ret = 0
        for w in words:
            mp[len(w)].add(w)

        # key: word, val: int
        word_with_length = {}

        for i in sorted(mp.keys()):
            next_word_with_length = {}
            for nxt_w in mp[i]:
                for j in range(len(nxt_w)):
                    new_w = nxt_w[:j] + nxt_w[j+1:]
                    next_word_with_length[nxt_w] = max(
                        next_word_with_length.get(nxt_w, 1),
                        word_with_length.get(new_w, 0) + 1
                    )
            word_with_length = next_word_with_length
            ret = max(ret, max(word_with_length.values()) if word_with_length.values() else 1)

        return ret
