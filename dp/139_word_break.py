# https://leetcode.com/problems/word-break/description/
# 139. Word Break

# History:
# Facebook
# 1.
# Feb 24, 2019
# 2.
# Nov 13, 2019
# 3.
# Feb 3, 2020
# 4.
# Apr 24, 2020

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


class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = {-1}

        for i in range(len(s)):
            for w in wordDict:
                if (i - len(w)) in dp and w == s[i - len(w) + 1:i + 1]:
                    dp.add(i)

        return (len(s) - 1) in dp


class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if (i - len(w) == -1 or dp[i - len(w)]) and s[i - len(w) + 1:i + 1] == w:
                    dp[i] = True
                    break

        return dp[-1]
