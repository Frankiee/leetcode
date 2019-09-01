# [DP-Array-Subsequence]
# https://leetcode.com/problems/shortest-common-supersequence/
# 1092. Shortest Common Supersequence

# Related:
# 1143. Longest Common Subsequence

# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return
# any of them.
#
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from
# T) results in the string S.)
#
#
#
# Example 1:
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
#
#
# Note:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        current_dp = [["", 0, None, None]] * len(str2)
        previous_dp = [["", 0, None, None]] * len(str2)

        for r in range(len(str1)):
            for c in range(len(str2)):
                if str1[r] == str2[c]:
                    if c >= 1 and r >= 1:
                        ret, lcs, str1_idx, str2_idx = previous_dp[c - 1]
                    else:
                        ret, lcs, str1_idx, str2_idx = "", 0, None, None

                    # append str1
                    start = str1_idx + 1 if str1_idx is not None else 0
                    ret += str1[start:r]

                    # append str2
                    start = str2_idx + 1 if str2_idx is not None else 0
                    ret += str2[start:c]

                    # append current element
                    ret += str1[r]

                    current_dp[c] = [ret, lcs + 1, r, c]
                else:
                    if r >= 1 and c >= 1:
                        if previous_dp[c][1] >= current_dp[c - 1][1]:
                            current_dp[c] = previous_dp[c]
                        else:
                            current_dp[c] = current_dp[c - 1]
                    elif r >= 1:
                        current_dp[c] = previous_dp[c]
                    else:
                        current_dp[c] = current_dp[c - 1]
            current_dp, previous_dp = previous_dp, current_dp

        ret, lcs, str1_idx, str2_idx = previous_dp[-1]

        # append str1
        start = str1_idx + 1 if str1_idx is not None else 0
        ret += str1[start:]

        # append str2
        start = str2_idx + 1 if str2_idx is not None else 0
        ret += str2[start:]

        return ret
