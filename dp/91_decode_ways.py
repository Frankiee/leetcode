# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways

# History:
# Facebook
# 1.
# May 17, 2019
# 2.
# Jan 30, 2020
# 3.
# Apr 6, 2020
# 4.
# May 15, 2020

# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6),
# or "BBF" (2 2 6).


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)

        for i in range(len(s)):
            if s[i] != '0':
                dp[i] += (dp[i - 1] if i >= 1 else 1)
            if i - 1 >= 0 and s[i - 1] != '0' and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += (dp[i - 2] if i - 2 >= 0 else 1)

        return dp[-1]


class SolutionDFS(object):
    def _dfs(self, s, i):
        if i == len(s):
            self.ret += 1
            return

        # 1 char
        if s[i] != '0':
            self._dfs(s, i + 1)

        # 2 char
        if s[i] != '0' and 10 <= int(s[i:i + 2]) <= 26:
            self._dfs(s, i + 2)

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.ret = 0
        self._dfs(s, 0)

        return self.ret
