# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 718. Maximum Length of Repeated Subarray

# History:
# 1.
# March 17, 2019
# 2.
# Nov 23, 2019

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
        dp = [None] * (len(A) + 1)
        for r in range(len(A) + 1):
            dp[r] = [0] * (len(B) + 1)

        max_so_far = 0
        for r in range(len(A) + 1):
            for c in range(len(B) + 1):
                if r > 0 and c > 0 and A[r - 1] == B[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                    max_so_far = max(max_so_far, dp[r][c])

        return max_so_far
