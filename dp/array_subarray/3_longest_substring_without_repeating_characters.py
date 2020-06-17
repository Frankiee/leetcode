# [Classic, DP-Array-Subarray]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters

# History:
# Facebook
# 1.
# Dec 15, 2019
# 2.
# Apr 22, 2020

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a
#              substring.


from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = defaultdict(int)
        repeated_count = 0
        ret = 0

        l = 0
        for idx, c in enumerate(s):
            counter[c] += 1

            if counter[c] > 1:
                repeated_count += 1

            while repeated_count > 0 and l < idx:
                counter[s[l]] -= 1
                if counter[s[l]] == 1:
                    repeated_count -= 1
                l += 1

            ret = max(ret, idx - l + 1)

        return ret
