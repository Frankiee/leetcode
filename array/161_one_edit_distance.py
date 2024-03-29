# https://leetcode.com/problems/one-edit-distance/
# 161. One Edit Distance

# History:
# Facebook
# 1.
# Jan 3, 2020
# 2.
# Apr 3, 2020

# Given two strings s and t, determine if they are both one edit distance apart.
#
# Note:
#
# There are 3 possiblities to satisify one edit distance apart:
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a 241character of s to get t
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:241
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.


class SolutionTwoPasses(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i + 1:]
        else:
            l, s = (s, t) if len(s) > len(t) else (t, s)

            if len(l) != len(s) + 1:
                return False

            for i in range(len(s)):
                if l[i] != s[i]:
                    return l[i + 1:] == s[i:]

        return True


class SolutionOnePass(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                if len(s) > len(t):
                    return s[i + 1:] == t[i:]
                if len(s) < len(t):
                    return s[i:] == t[i + 1:]

        return abs(len(s) - len(t)) == 1
