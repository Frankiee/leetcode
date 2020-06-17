# [Classic, Bisect-Lower-Bound]
# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence

# History:
# Facebook
# 1.
# March 17, 2019
# 2.
# Nov 21, 2019
# 3.
# Feb 3, 2020
# 4.
# May 5, 2020

# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore
# the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


class SolutionBinarySearch(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = [0] * len(nums)
        size = 0

        for n in nums:
            l, r = 0, size

            while l < r:
                m = (r - l) / 2 + l

                if tail[m] >= n:
                    r = m
                else:
                    l = m + 1

            tail[l] = n
            size = max(size, l + 1)

        return size


# WARNING: Better solution exists
class SolutionDP(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        ret = 1
        for r in range(1, len(nums)):
            for l in range(r):
                if nums[r] > nums[l]:
                    dp[r] = max(dp[r], dp[l] + 1)

            ret = max(dp[r], ret)

        return ret
