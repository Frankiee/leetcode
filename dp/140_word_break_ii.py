# [Important]
# https://leetcode.com/problems/word-break-ii/
# 140. Word Break II

# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word
# is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


class Solution(object):
    def dfs(self, ret, i, prefix, dp):
        if i == -1:
            ret.append(' '.join(prefix))
        if i < 0:
            return

        for w in list(dp[i]):
            prefix.insert(0, w)
            self.dfs(ret, i - len(w), prefix, dp)
            prefix.pop(0)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = []
        for i in range(len(s)):
            dp.append(set())

        for i in range(len(s)):
            for w in wordDict:
                back_i = i - len(w)
                if ((back_i == -1 or (back_i >= 0 and dp[back_i])) and
                        s[back_i + 1:i + 1] == w):
                    dp[i].add(w)

        ret = []

        if dp[len(s) - 1]:
            self.dfs(ret, len(s) - 1, [], dp)

        return ret
