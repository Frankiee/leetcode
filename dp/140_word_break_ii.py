# https://leetcode.com/problems/word-break-ii/
# 140. Word Break II

# History:
# Facebook
# 1.
# Aug 18, 2019
# 2.
# Mar 12, 2020
# 3.
# Apr 24, 2020

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


class SolutionDP(object):
    def _dfs(self, s, wordDict, i, curr, ret, dp):
        if i == -1:
            ret.append(
                " ".join(reversed(curr))
            )
            return

        for w in wordDict:
            if ((i - len(w) == -1 or (i - len(w) >= 0 and dp[i - len(w)])) and
                    s[i - len(w) + 1:i + 1] == w):
                self._dfs(s, wordDict, i - len(w), curr + [w], ret, dp)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if (i - len(w) == -1 or dp[i - len(w)]) and s[i - len(w) + 1:i + 1] == w:
                    dp[i] = True
                    break

        if not dp[-1]:
            return []

        ret = []

        self._dfs(s, wordDict, len(s) - 1, [], ret, dp)

        return ret


class SolutionDPSet(object):
    def _dfs(self, s, wordDict, ret, curr_result, curr_idx, dp):
        if curr_idx < 0:
            ret.append(curr_result)
            return

        for w_i in dp[curr_idx]:
            self._dfs(
                s,
                wordDict,
                ret,
                wordDict[w_i] + " " + curr_result if curr_result else wordDict[w_i],
                curr_idx - len(wordDict[w_i]),
                dp,
            )

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [set() for _ in range(len(s))]

        for i in range(len(s)):
            for w_i, w in enumerate(wordDict):
                if ((i - len(w) == -1 or (i >= len(w) and dp[i - len(w)])) and
                        s[i - len(w) + 1:i + 1] == w):
                    dp[i].add(w_i)

        if not dp[-1]:
            return []

        ret = []
        self._dfs(s, wordDict, ret, "", len(s) - 1, dp)
        return ret
