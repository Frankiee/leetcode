# https://leetcode.com/problems/find-the-difference/
# 389. Find the Difference

# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ret = 0

        for c in s + t:
            ret ^= ord(c)

        return chr(ret)
