# https://leetcode.com/problems/distinct-subsequences/description/
# 115. Distinct Subsequences

# Given a string S and a string T, count the number of distinct subsequences
# of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s = len(s)
        len_t = len(t)

        memory = [None] * (len_t + 1)
        for r in range(len_t + 1):
            memory[r] = [None] * (len_s + 1)

        for r in range(len_t + 1):
            for c in range(len_s + 1):
                if r == 0:
                    memory[r][c] = 1
                elif c == 0:
                    memory[r][c] = 0
                else:
                    if s[c - 1] == t[r - 1]:
                        memory[r][c] = memory[r][c - 1] + memory[r - 1][c - 1]
                    else:
                        memory[r][c] = memory[r][c - 1]

        return memory[len_t][len_s]
