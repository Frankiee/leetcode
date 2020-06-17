# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# 159. Longest Substring with At Most Two Distinct Characters

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# Apr 23, 2020

# Given a string s , find the length of the longest substring t  that contains at most 2 distinct
# characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.


from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct_count = 0
        counter = defaultdict(int)

        ret = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1

            if counter[s[r]] == 1:
                distinct_count += 1

            while distinct_count > 2:
                counter[s[l]] -= 1

                if counter[s[l]] == 0:
                    distinct_count -= 1
                l += 1

            ret = max(ret, r - l + 1)

        return ret
