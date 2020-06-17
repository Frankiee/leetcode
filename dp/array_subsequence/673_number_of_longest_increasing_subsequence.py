# [DP-Array-Subsequence]
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# 673. Number of Longest Increasing Subsequence

# History:
# 1.
# May 12, 2019
# 2.
# Nov 21, 2019

# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [
# 1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [(1, 1)] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
                    elif dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, dp[j][1])

        max_length = max([n[0] for n in dp])

        return sum([n[1] for n in dp if n[0] == max_length])
