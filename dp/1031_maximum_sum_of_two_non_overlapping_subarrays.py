# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# 1031. Maximum Sum of Two Non-Overlapping Subarrays

# History:
# Google
# 1.
# Mar 15, 2020

# Given an array A of non-negative integers, return the maximum sum of elements in two
# non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification,
# the L-length subarray could occur before or after the M-length subarray.)
#
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1]
# + ... + A[j+M-1]) and either:
#
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
#
#
# Example 1:
#
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
# Example 2:
#
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
# Example 3:
#
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
#
#
# Note:
#
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        m_dp = [None] * len(A)

        curr_sum = 0
        curr_val = 0
        for i in range(len(A) - 1, -1, -1):
            curr_sum += A[i]
            if i < len(A) - M:
                curr_sum -= A[i + M]

            if i > len(A) - M:
                curr_val = 0
            else:
                curr_val = curr_sum

            m_dp[i] = max(curr_val, m_dp[i + 1]) if i < len(A) - 1 else curr_val

        ret = 0
        curr_l_sum = 0
        left_max_m_sum = 0
        curr_left_m_sum = 0
        for i in range(len(A)):
            curr_l_sum += A[i]
            if i >= L:
                curr_l_sum -= A[i - L]

            if i < L - 1:
                left_sum = 0
            else:
                left_sum = curr_l_sum

            if i >= L:
                curr_left_m_sum += A[i - L]

                if i >= L + M:
                    curr_left_m_sum -= A[i - L - M]

            if i >= L + M - 1:
                left_max_m_sum = max(left_max_m_sum, curr_left_m_sum)

            ret = max(ret, left_sum + max(m_dp[i + 1] if i < len(A) - 1 else 0, left_max_m_sum))

        return ret
