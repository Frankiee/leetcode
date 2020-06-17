# [Classic]
# https://leetcode.com/problems/is-subsequence/
# 392. Is Subsequence

# Related:
# 792. Number of Matching Subsequences

# History:
# TikTok
# 1.
# Aug, 24, 2020
# 2.
# Apr 26, 2020

# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and
# t. t is potentially a very long (length ~= 500,000) string, and s is a
# short string (<=100).
#
# A subsequence of a string is a new string which is formed from the
# original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (ie,
# "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
# Return false.
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence. In this
# scenario, how would you change your code?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.


from collections import defaultdict


class SolutionBisect(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_indices = defaultdict(list)

        for i, c in enumerate(t):
            char_indices[c].append(i)

        curr_idx = -1
        for c in s:
            lst = char_indices[c]

            nxt_idx = bisect.bisect_left(lst, curr_idx)

            if nxt_idx >= len(lst):
                return False

            curr_idx = lst[nxt_idx] + 1

        return True


class SolutionLinear(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False

        s_idx = t_idx = 0
        while t_idx < len(t):
            while s[s_idx] != t[t_idx]:
                t_idx += 1
                if t_idx == len(t):
                    return False

            t_idx += 1
            s_idx += 1
            if s_idx == len(s):
                return True

        return False
