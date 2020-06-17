# https://leetcode.com/problems/isomorphic-strings/
# 205. Isomorphic Strings

# History:
# Google, Facebook
# 1.
# Mar 10, 2020
# 2.
# May 3, 2020

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the
# order of characters. No two characters may map to the same character but a character may map to
# itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.


class SolutionDictSet(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mp = {}
        mapped = set()

        for i in range(len(s)):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped:
                    return False

            mp[s[i]] = t[i]
            mapped.add(t[i])

        return True


class SolutionTwoDict(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        forward, reverse = {}, {}

        for i in range(len(s)):
            s_c, t_c = s[i], t[i]

            if s_c in forward and forward[s_c] != t_c:
                return False
            if t_c in reverse and reverse[t_c] != s_c:
                return False

            forward[s_c] = t_c
            reverse[t_c] = s_c

        return True
