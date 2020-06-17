# [DP-Array-Subarray, Classic]
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# 689. Maximum Sum of 3 Non-Overlapping Subarrays

# History:
# Google
# 1.
# Mar 26, 2020
# 2.
# Apr 6, 2020
# 3.
# May 14, 2020

# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (
# 0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
# Example:
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
#
# Note:
#
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix_sum = [None] * (len(nums) + 1)
        prefix_sum[0] = 0
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [[(0, None)] * len(nums) for _ in range(3)]

        for r in range(3):
            for l in range(k * (r + 1) - 1, len(nums)):
                new_val = (
                    (dp[r - 1][l - k][0] if l - k >= 0 and r - 1 >= 0 else 0) +
                    prefix_sum[l + 1] - prefix_sum[l - k + 1]
                )
                if new_val > dp[r][l - 1][0]:
                    dp[r][l] = (new_val, l - k + 1)
                else:
                    dp[r][l] = dp[r][l - 1]

        ret = []
        idx = -1
        for r in range(2, -1, -1):
            _, idx = dp[r][idx]
            ret.append(idx)
            idx -= 1
        return reversed(ret)


class SolutionRollingSum(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left_max_sum = [(0, None)] * len(nums)

        curr_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if i > k - 1:
                curr_sum -= nums[i - k]
            if curr_sum > max_sum:
                max_sum, max_idx = curr_sum, i
            else:
                max_sum, max_idx = left_max_sum[i - 1]
            if i >= k - 1:
                left_max_sum[i] = (max_sum, max_idx)

        right_max_sum = [(0, None)] * len(nums)

        curr_sum = 0
        max_sum = 0
        ret = None
        ret_max = 0
        for i in range(len(nums) - 1, -1, -1):
            curr_sum += nums[i]
            if i < len(nums) - k:
                curr_sum -= nums[i + k]
            if curr_sum >= max_sum:
                max_sum, max_idx = curr_sum, i
            else:
                max_sum, max_idx = right_max_sum[i + 1]
            if i <= len(nums) - k:
                right_max_sum[i] = (max_sum, max_idx)

            if k <= i < len(nums) - k:
                new_total = curr_sum + left_max_sum[i - 1][0] + right_max_sum[i + k][0]
                if new_total >= ret_max:
                    ret_max = new_total
                    ret = (left_max_sum[i - 1][1] - k + 1, i, right_max_sum[i + k][1])

        return ret
