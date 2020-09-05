# https://leetcode.com/problems/edit-distance/
# 72. Edit Distance

# History:
# Google
# 1.
# March 17, 2019
# 2.
# Nov 23, 2019
# 3.
# Mar 17, 2020
# 4.
# Aug 3, 2020

# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]

        for r in range(word1_len + 1):
            for c in range(word2_len + 1):
                if r == 0 or c == 0:
                    dp[r][c] = max(r, c)
                else:
                    if word1[r - 1] == word2[c - 1]:
                        dp[r][c] = dp[r - 1][c - 1]
                    else:
                        dp[r][c] = min([
                            dp[r - 1][c],
                            dp[r][c - 1],
                            dp[r - 1][c - 1],
                        ]) + 1

        return dp[-1][-1]
