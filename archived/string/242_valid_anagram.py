# [Archived]
# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram

# History:
# Facebook
# 1.
# May 2, 2020

# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = Counter(s)

        for c in t:
            counter[c] -= 1

            if counter[c] < 0:
                return False
            if counter[c] == 0:
                del counter[c]

        return not bool(counter)
