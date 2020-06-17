# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String

# History:
# Facebook
# 1.
# Mar 31, 2019
# 2.
# Apr 22, 2020

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for s1_i in range(len(s1) + 1):
            for s2_i in range(len(s2) + 1):
                if s1_i == s2_i == 0:
                    dp[s1_i][s2_i] = True
                else:
                    if s1_i > 0 and s1[s1_i - 1] == s3[s1_i + s2_i - 1]:
                        dp[s1_i][s2_i] = dp[s1_i - 1][s2_i]

                    if s2_i > 0 and s2[s2_i - 1] == s3[s1_i + s2_i - 1]:
                        dp[s1_i][s2_i] = dp[s1_i][s2_i] or dp[s1_i][s2_i - 1]

        return dp[-1][-1]
