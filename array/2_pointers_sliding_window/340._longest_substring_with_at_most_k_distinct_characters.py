# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# 340. Longest Substring with At Most K Distinct Characters

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# May 4, 2020

# Given a string, find the length of the longest substring T that contains at most k distinct
# characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.


from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = defaultdict(int)
        unique_counter = 0

        ret = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            if counter[s[r]] == 1:
                unique_counter += 1

            while unique_counter > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    unique_counter -= 1
                l += 1

            ret = max(ret, r - l + 1)

        return ret
