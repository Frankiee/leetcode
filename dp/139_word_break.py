# [Important]
# https://leetcode.com/problems/word-break/description/
# 139. Word Break

# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as
# "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if (i - len(w) == -1 or
                        (i - len(w) >= 0 and dp[i - len(w)])) and (
                        s[i - len(w) + 1:i + 1]) == w:
                    dp[i] = True

        return dp[-1]
