# [Classic]
# https://leetcode.com/problems/longest-word-in-dictionary/
# 720. Longest Word in Dictionary

# History:
# Google
# 1.
# Mar 12, 2020

# Given a list of strings words representing an English Dictionary, find the longest word in
# words that can be built one character at a time by other words in words. If there is more than
# one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is
# lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].


from collections import defaultdict


class Solution(object):
    CHARS = 'abcdefghijklmnopqrstuvwxyz'

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        mp = defaultdict(set)

        longest_length = 0
        for w in words:
            mp[len(w)].add(w)
            longest_length = max(longest_length, len(w))

        word_with_len = set()
        for i in range(1, longest_length + 2):
            if not mp[i]:
                if not word_with_len:
                    return ""
                return sorted(list(word_with_len))[0]

            if i == 1:
                word_with_len = mp[i]
            else:
                nxt_word_with_len = set()

                for w in word_with_len:
                    for c in self.CHARS:
                        new_w = w + c
                        if new_w in mp[i]:
                            nxt_word_with_len.add(new_w)

                if not nxt_word_with_len:
                    if not word_with_len:
                        return ""
                    return sorted(list(word_with_len))[0]

                word_with_len = nxt_word_with_len
