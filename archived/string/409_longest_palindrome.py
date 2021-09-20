# [Archived]
# https://leetcode.com/problems/longest-palindrome/
# 409. Longest Palindrome

# History:
# 1.
# Sep 14, 2019

# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)

        ret = 0
        used_single = False
        for c, freq in counter.iteritems():
            if freq % 2 == 1 and not used_single:
                ret += freq
                used_single = True
            else:
                ret += freq - (freq % 2)

        return ret
