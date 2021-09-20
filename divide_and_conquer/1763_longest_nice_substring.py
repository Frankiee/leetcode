# https://leetcode.com/problems/longest-nice-substring/
# 1763. Longest Nice Substring

# History:
# Microsoft
# 1.
# Apr 11, 2021

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear.
# However, "abA" is not because 'b' appears, but 'B' does not.
#
# Given a string s, return the longest substring of s that is nice.
# If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
#
#
#
# Example 1:
#
# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s,
# and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# Example 2:
#
# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Example 3:
#
# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.
# Example 4:
#
# Input: s = "dDzeE"
# Output: "dD"
# Explanation: Both "dD" and "eE" are the longest nice substrings.
# As there are multiple longest nice substrings, return "dD" since it occurs earlier.
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of uppercase and lowercase English letters.

# log(n) rounds in total, and overall complexity is O(nlog(n))
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        all_chars = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in all_chars:
                s_left = self.longestNiceSubstring(s[:i])
                s_right = self.longestNiceSubstring(s[i + 1:])

                if len(s_left) >= len(s_right):
                    return s_left
                else:
                    return s_right

        return s
