# [Classic, DP-Array-Subarray, Palindrome]
# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring

# History:
# Facebook
# 1.
# Nov 29, 2019
# 2.
# Jan 4, 2020
# 3.
# May 12, 2020

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum
# length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        ret = s[0]

        to_check = []
        for i in range(len(s)):
            nxt_to_check = []

            nxt_to_check.append(i)
            if i - 1 >= 0:
                nxt_to_check.append(i - 1)

            for p_idx in to_check:
                if s[p_idx] == s[i]:
                    if i - p_idx + 1 > len(ret):
                        ret = s[p_idx:i + 1]

                    if p_idx - 1 >= 0:
                        nxt_to_check.append(p_idx - 1)

            to_check = nxt_to_check

        return ret
