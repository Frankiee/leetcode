# [Classic]
# https://leetcode.com/problems/shortest-palindrome/
# 214. Shortest Palindrome

# History:
# Facebook
# 1.
# Mar 29, 2020
# 2.
# May 12, 2020

# Given a string s, you are allowed to convert it to a palindrome by adding characters in front
# of it. Find and return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: "abcd"
# Output: "dcbabcd"


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s), -1, -1):
            candidate = s[:i][::-1]

            if s[:i] == candidate:
                return s[i:][::-1] + s
