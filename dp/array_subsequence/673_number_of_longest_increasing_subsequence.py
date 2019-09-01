# [NonContiguousSubarray]
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# 673. Number of Longest Increasing Subsequence

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

        max_len = 1
        dp = [1] * len(nums)
        dp_count = [1] * len(nums)

        for idx in range(1, len(nums)):
            for p in range(idx):
                if nums[idx] > nums[p]:
                    current_len = dp[p] + 1
                    if dp[idx] == current_len:
                        dp_count[idx] += dp_count[p]
                    elif current_len > dp[idx]:
                        dp_count[idx] = dp_count[p]

                    max_len = max(max_len, current_len)
                    dp[idx] = max(dp[idx], current_len)

        return sum([dp_count[i] for i in range(len(dp)) if dp[i] == max_len])
