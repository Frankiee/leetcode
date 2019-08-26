# [DP-Sequence-Action-Groups]
# https://leetcode.com/problems/largest-sum-of-averages/
# 813. Largest Sum of Averages

# https://www.youtube.com/watch?v=IPdShoUE9z8
# Related: 312. Burst Balloons

# We partition a row of numbers A into at most K adjacent (non-empty)
# groups, then our score is the sum of the average of each group. What is
# the largest score we can achieve?
#
# Note that our partition must use every number in A, and that scores are
# not necessarily integers.
#
# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is
# 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
#
# Note:
#
# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # row: number of groups starting from 1
        # column: first ith elements in A
        dp = [None] * K
        rolling_sum = [0] * len(A)

        for k in range(K):
            dp[k] = [float('-inf')] * len(A)

        for k in range(K):
            for i in range(len(A)):
                if k == 0:
                    rolling_sum[i] = rolling_sum[i - 1] + A[i]
                    dp[k][i] = float(rolling_sum[i]) / (i + 1)
                elif i >= k:
                    for j in range(k - 1, i):
                        dp[k][i] = max(
                            dp[k - 1][j] + float(
                                rolling_sum[i] - rolling_sum[j]) / (i - j),
                            dp[k][i],
                        )

        return dp[K - 1][len(A) - 1]
