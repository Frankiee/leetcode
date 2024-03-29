# https://leetcode.com/problems/repeated-substring-pattern/description/
# 459. Repeated Substring Pattern

# History:
# Google
# 1.
# Feb 11, 2019
# 2.
# Nov 17, 2019
# 3.
# Mar 11, 2020

# Given a non-empty string check if it can be constructed by taking a
# substring of it and appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only
# and its length will not exceed 10000.
#
# Example 1:
#
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:
#
# Input: "aba"
# Output: False
# Example 3:
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring
# "abcabc" twice.)


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        return s in (s + s)[1:-1]
