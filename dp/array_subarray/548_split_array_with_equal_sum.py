# [DP-Array-Subarray, Classic]
# https://leetcode.com/problems/split-array-with-equal-sum/
# 548. Split Array with Equal Sum

# History:
# Facebook
# 1.
# May 11, 2020

# Given an array with n integers, you need to find if there are triplets (i, j, k) which
# satisfies following conditions:
#
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting from the
# element indexed L to the element indexed R.
# Example:
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5.
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# Note:
# 1 <= n <= 2000.
# Elements in the given array will be in range [-1,000,000, 1,000,000].


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prefix_sum = [0] * len(nums)

        for i, n in enumerate(nums):
            prefix_sum[i] = (prefix_sum[i - 1] if i > 0 else 0) + n

        for m_i in range(3, len(nums) - 3):
            left_half_sum = prefix_sum[m_i - 1]
            right_half_sum = prefix_sum[-1] - prefix_sum[m_i]

            left_sum = set()
            for l_i in range(1, m_i - 1):
                left = prefix_sum[l_i - 1] if l_i - 1 >= 0 else 0
                right = left_half_sum - left - nums[l_i]

                if left == right:
                    left_sum.add(left)

            for r_i in range(m_i + 2, len(nums) - 1):
                left = prefix_sum[r_i - 1] - prefix_sum[m_i]
                right = right_half_sum - left - nums[r_i]

                if left == right and left in left_sum:
                    return True

        return False


class SolutionDP(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prefix_sum = [0] * len(nums)

        for i, n in enumerate(nums):
            prefix_sum[i] = (prefix_sum[i - 1] if i > 0 else 0) + n

        dp = [[set() for _ in range(len(nums))] for _ in range(4)]

        for division in range(4):
            for i in range(len(nums)):
                if division == 0:
                    dp[division][i].add(prefix_sum[i])
                else:
                    for last_d in range(i):
                        if (last_d - 1 >= 0 and
                                (prefix_sum[i] - prefix_sum[last_d]) in
                                dp[division - 1][last_d - 1]):
                            dp[division][i].add(prefix_sum[i] - prefix_sum[last_d])

        return bool(dp[3][-1])
