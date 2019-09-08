# [Archived]
# https://leetcode.com/problems/maximum-average-subarray-i/
# 643. Maximum Average Subarray I

# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output
# the maximum average value.
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
#
#
# Note:
#
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        rolling_sum = sum(nums[:k])
        c_max = rolling_sum / float(k)

        for i in range(k, len(nums)):
            rolling_sum += nums[i]
            rolling_sum -= nums[i - k]

            c_max = max(c_max, rolling_sum / float(k))

        return c_max
