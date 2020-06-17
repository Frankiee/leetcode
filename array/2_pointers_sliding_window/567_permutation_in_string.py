# https://leetcode.com/problems/permutation-in-string/
# 567. Permutation in String

# History:
# Facebook
# 1.
# Mar 2, 2020
# 2.
# May 4, 2020

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of
# s1. In other words, one of the first string's permutations is the substring of the second string.
#
#
#
# Example 1:
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
# Note:
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

from collections import Counter, defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        char_diff = len(s1)

        l = 0
        for r, c in enumerate(s2):
            s2_counter[c] += 1
            if s2_counter[c] <= s1_counter[c]:
                char_diff -= 1

            if r >= len(s1):
                s2_counter[s2[l]] -= 1
                if s2_counter[s2[l]] < s1_counter[s2[l]]:
                    char_diff += 1

                l += 1

            if r >= len(s1) - 1:
                if char_diff == 0:
                    return True

        return False
