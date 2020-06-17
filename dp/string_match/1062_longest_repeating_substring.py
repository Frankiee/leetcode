# [Classic, String-Match]
# https://leetcode.com/problems/longest-repeating-substring/
# 1062. Longest Repeating Substring

# History:
# Facebook
# 1.
# May 5, 2020

# Given a string S, find out the length of the longest repeating substring(s). Return 0 if no
# repeating substring exists.
#
#
#
# Example 1:
#
# Input: "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# Example 2:
#
# Input: "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
# Example 3:
#
# Input: "aabcaab
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
# Example 4:
#
# Input: "aaaaa"
# Output: 4
# Explanation: The longest repeating substring is "aaaa", which occurs twice.
#
#
# Note:
#
# The string S consists of only lowercase English letters from 'a' - 'z'.
# 1 <= S.length <= 1500


class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [[0] * (len(S) + 1) for _ in range(len(S) + 1)]

        ret = 0
        for r_idx_plus_one in range(len(S) + 1):
            for l_idx_plus_one in range(r_idx_plus_one):
                if l_idx_plus_one > 0 and r_idx_plus_one > 0:
                    if S[l_idx_plus_one - 1] == S[r_idx_plus_one - 1]:
                        dp[l_idx_plus_one][r_idx_plus_one] = 1 + dp[l_idx_plus_one - 1][
                            r_idx_plus_one - 1]
                        ret = max(ret, dp[l_idx_plus_one][r_idx_plus_one])

        return ret
