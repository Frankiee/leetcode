# [DP-Array-Subsequence]
# https://leetcode.com/problems/longest-common-subsequence/
# 1143. Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest
# common subsequence.
#
# A subsequence of a string is a new string generated from the original
# string with some characters(can be none) deleted without changing the
# relative order of the remaining characters. (eg, "ace" is a subsequence of
# "abcde" while "aec" is not). A common subsequence of two strings is a
# subsequence that is common to both strings.
#
#
#
# If there is no common subsequence, return 0.
#
#
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
# Constraints:
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0

        current_dp = [0] * len(text2)
        previous_dp = [0] * len(text2)

        for r in range(len(text1)):
            for c in range(len(text2)):
                if text1[r] == text2[c]:
                    current_dp[c] = (
                        previous_dp[c - 1] + 1
                        if r >= 1 and c >= 1
                        else 1
                    )
                else:
                    current_dp[c] = max(
                        previous_dp[c] if r >= 1 else 0,
                        current_dp[c - 1] if c >= 1 else 0,
                    )

            current_dp, previous_dp = previous_dp, current_dp

        return previous_dp[-1]
