# [Classic, String-Match]
# https://leetcode.com/problems/regular-expression-matching/
# 10. Regular Expression Matching

# History:
# Facebook
# 1.
# Apr 5, 2020
# 2.
# Apr 7, 2020
# 3.
# Apr 26, 2020
# 4.
# May 12, 2020

# Explanation
# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest

# Given an input string (s) and a pattern (p), implement regular expression matching with support
# for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
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
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a'
# once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


class SolutionDP(object):
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
                elif p_i_p_one == 0:
                    dp[s_i_p_one][p_i_p_one] = False
                elif s_i_p_one == 0:
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one][p_i_p_one - 2] and p[p_i_p_one - 1] == '*'
                    )
                elif p[p_i_p_one - 1] == '.':
                    dp[s_i_p_one][p_i_p_one] = dp[s_i_p_one - 1][p_i_p_one - 1]
                elif p[p_i_p_one - 1] == '*':
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one][p_i_p_one - 1] or dp[s_i_p_one][p_i_p_one - 2]
                    )

                    if s[s_i_p_one - 1] == p[p_i_p_one - 2] or p[p_i_p_one - 2] == '.':
                        dp[s_i_p_one][p_i_p_one] = (
                            dp[s_i_p_one][p_i_p_one] or dp[s_i_p_one - 1][p_i_p_one])
                else:
                    dp[s_i_p_one][p_i_p_one] = (
                        dp[s_i_p_one - 1][p_i_p_one - 1] and s[s_i_p_one - 1] == p[p_i_p_one - 1]
                    )

        return dp[-1][-1]


class SolutionDP2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        dp[0][0] = True

        for p_i in range(2, len(p) + 1):
            dp[p_i][0] = dp[p_i - 2][0] and p[p_i - 1] == '*'

        for p_i in range(1, len(p) + 1):
            for s_i in range(1, len(s) + 1):
                if p[p_i - 1] != '*':
                    dp[p_i][s_i] = dp[p_i - 1][s_i - 1] and (
                            s[s_i - 1] == p[p_i - 1] or p[p_i - 1] == '.')
                else:
                    dp[p_i][s_i] = dp[p_i - 1][s_i] or dp[p_i - 2][s_i]

                    if s[s_i - 1] == p[p_i - 2] or p[p_i - 2] == '.':
                        dp[p_i][s_i] |= dp[p_i][s_i - 1]

        return dp[-1][-1]
