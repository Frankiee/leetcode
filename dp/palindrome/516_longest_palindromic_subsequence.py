# [DP-Array-Subsequence, Classic, Palindrome]
# https://leetcode.com/problems/longest-palindromic-subsequence/
# 516. Longest Palindromic Subsequence

# History:
# Facebook
# 1.
# Dec 1, 2019
# 2.
# Jan 4, 2020
# 3.
# Match 29, 2020

# Given a string s, find the longest palindromic subsequence's length in s. You may assume that
# the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_minus_one = None
        dp_minus_two = None

        for length in range(1, len(s) + 1):
            current_dp = {}

            for i in range(len(s) - length + 1):
                if length == 1:
                    current_dp[i] = 1
                elif length == 2:
                    current_dp[i] = 2 if s[i] == s[i + 1] else 1
                elif s[i] == s[i + length - 1]:
                    current_dp[i] = dp_minus_two[i + 1] + 2
                else:
                    current_dp[i] = max(
                        dp_minus_one[i],
                        dp_minus_one[i + 1],
                    )

            dp_minus_one, dp_minus_two = current_dp, dp_minus_one

        return dp_minus_one[0]


class SolutionMoreMemory(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[None] * len(s) for _ in range(len(s))]

        for length in range(1, len(s) + 1):
            for l in range(len(s) - length + 1):
                r = l + length - 1
                if length == 1:
                    dp[l][r] = 1
                elif length == 2:
                    if s[l] == s[r]:
                        dp[l][r] = 2
                    else:
                        dp[l][r] = 1
                else:
                    dp[l][r] = max(
                        dp[l + 1][r],
                        dp[l][r - 1],
                    )
                    if s[l] == s[r] and l + 1 <= r - 1:
                        dp[l][r] = max(dp[l][r], dp[l + 1][r - 1] + 2)

        return dp[0][-1]
