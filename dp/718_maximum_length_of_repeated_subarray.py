# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 718. Maximum Length of Repeated Subarray

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
        if not A or not B:
            return 0

        max_length = 0

        len_a, len_b = len(A), len(B)

        dp = [None] * (len_a + 1)
        for r in range(len_a + 1):
            dp[r] = [0] * (len_b + 1)

        for r in range(len_a + 1):
            for c in range(len_b + 1):
                if r == 0 or c == 0:
                    dp[r][c] = 0
                else:
                    if A[r - 1] == B[c - 1]:
                        dp[r][c] = dp[r - 1][c - 1] + 1
                        max_length = max(max_length, dp[r][c])

        return max_length
