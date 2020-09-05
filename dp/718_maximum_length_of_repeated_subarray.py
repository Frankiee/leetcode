# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 718. Maximum Length of Repeated Subarray

# History:
# Google
# 1.
# March 17, 2019
# 2.
# Nov 23, 2019
# 3.
# Jun 23, 2020

# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        ret = 0
        for a_i_plus_one in range(len(A) + 1):
            for b_i_plus_one in range(len(A) + 1):
                if (a_i_plus_one > 0 and b_i_plus_one > 0 and
                        A[a_i_plus_one - 1] == B[b_i_plus_one - 1]):
                    dp[a_i_plus_one][b_i_plus_one] = dp[a_i_plus_one - 1][b_i_plus_one - 1] + 1
                    ret = max(ret, dp[a_i_plus_one][b_i_plus_one])

        return ret
