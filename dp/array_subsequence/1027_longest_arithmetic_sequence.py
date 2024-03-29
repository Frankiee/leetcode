# [DP-Array-Subsequence]
# https://leetcode.com/problems/longest-arithmetic-sequence/
# 1027. Longest Arithmetic Sequence

# History:
# Facebook
# 1.
# Dec 15, 2019
# 2.
# May 2, 2020

# Given an array A of integers, return the length of the longest arithmetic subsequence in A.
#
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ...
# < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same
# value (for 0 <= i < B.length - 1).
#
#
#
# Example 1:
#
# Input: [3,6,9,12]
# Output: 4
# Explanation:
# The whole array is an arithmetic sequence with steps of length = 3.
# Example 2:
#
# Input: [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].
# Example 3:
#
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].
#
#
# Note:
#
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [{} for _ in range(len(A))]

        ret = 0
        for i in range(len(A)):
            for j in range(i):
                step = A[i] - A[j]

                if step in dp[j]:
                    dp[i][step] = dp[j][step] + 1
                else:
                    dp[i][step] = 2

                ret = max(ret, dp[i][step])

        return ret
