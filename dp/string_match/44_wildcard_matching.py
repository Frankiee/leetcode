# [Classic, String-Match]
# https://leetcode.com/problems/wildcard-matching/
# 44. Wildcard Matching

# History:
# Facebook, TikTok
# 1.
# Mar 8, 2020
# 2.
# Apr 26, 2020

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support
# for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the
# substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        for s_i_p_one in range(len(s) + 1):
            for p_i_p_one in range(len(p) + 1):
                if s_i_p_one == p_i_p_one == 0:
                    dp[s_i_p_one][p_i_p_one] = True
                elif s_i_p_one == 0:
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one][p_i_p_one - 1] and
                        p[p_i_p_one - 1] == '*'
                    )
                elif p_i_p_one == 0:
                    dp[s_i_p_one][p_i_p_one] = False
                elif p[p_i_p_one - 1] == '?':
                    dp[s_i_p_one][p_i_p_one] = dp[s_i_p_one - 1][p_i_p_one - 1]
                elif p[p_i_p_one - 1] == '*':
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one][p_i_p_one - 1] or
                        dp[s_i_p_one - 1][p_i_p_one]
                    )
                else:
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one - 1][p_i_p_one - 1] and
                        p[p_i_p_one - 1] == s[s_i_p_one - 1]
                    )

        return dp[-1][-1]
