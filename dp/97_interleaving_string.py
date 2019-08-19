# [Important]
# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String

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
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3

        dp = [False] * (len(s1) + 1)
        for r in range(len(s1) + 1):
            dp[r] = [False] * (len(s2) + 1)

        for r in range(len(s1) + 1):
            for c in range(len(s2) + 1):
                if r == 0 and c == 0:
                    dp[r][c] = True
                else:
                    dp[r][c] = (
                        # next char comes from s1
                        r != 0 and dp[r - 1][c] and s3[r + c - 1] == s1[r - 1]
                    ) or (
                        # next char comes from s2
                        c != 0 and dp[r][c - 1] and s3[r + c - 1] ==
                        s2[c - 1]
                    )

        return dp[len(s1)][len(s2)]
