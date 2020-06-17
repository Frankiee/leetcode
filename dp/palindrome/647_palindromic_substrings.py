# [DP-Array-Subarray, Classic, Palindrome]
# https://leetcode.com/problems/palindromic-substrings/
# 647. Palindromic Substrings

# History:
# Facebook
# 1.
# Sep 14, 2019
# 2.
# Jan 4, 2020
# 3.
# May 2, 2020

# Given a string, your task is to count how many palindromic substrings in
# this string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Note:
#
# The input string length won't exceed 1000.


class Solution2DDP(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]

        ret = 0
        for l in range(1, len(s) + 1):
            for start in range(len(s) - l + 1):
                end = start + l - 1
                if l == 1:
                    dp[start][end] = True
                    ret += 1
                elif l == 2:
                    if s[start] == s[end]:
                        dp[start][end] = True
                        ret += 1
                else:
                    if s[start] == s[end] and dp[start + 1][end - 1]:
                        dp[start][end] = True
                        ret += 1

        return ret


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        to_checks = []

        for i in range(len(s)):
            nxt_to_checks = []

            ret += 1

            nxt_to_checks.append(i)
            if i > 0:
                nxt_to_checks.append(i - 1)

            for c in to_checks:
                if s[i] == s[c]:
                    ret += 1
                    if c - 1 >= 0:
                        nxt_to_checks.append(c - 1)

            to_checks = nxt_to_checks

        return ret
