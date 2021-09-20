# [Archived]
# https://leetcode.com/problems/merge-strings-alternately/
# 1768. Merge Strings Alternately

# History:
# 1.
# Apr 11, 2021

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# Python 3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pt = word2_pt = 0
        is_word1 = True

        ret = []

        while word1_pt < len(word1) or word2_pt < len(word2):
            if is_word1 and word1_pt < len(word1):
                ret.append(word1[word1_pt])
                word1_pt += 1
                is_word1 = False
            elif not is_word1 and word2_pt < len(word2):
                ret.append(word2[word2_pt])
                word2_pt += 1
                is_word1 = True
            elif word1_pt < len(word1):
                ret.append(word1[word1_pt])
                word1_pt += 1
            else:
                ret.append(word2[word2_pt])
                word2_pt += 1

        return "".join(ret)
