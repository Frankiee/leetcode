# [DP-Array-Subarray]
# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

# Related:
# 1186. Maximum Subarray Sum with One Deletion

# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = dp_with_last = float('-inf')

        for n in nums:
            dp_with_last = max(n, n + dp_with_last)
            ret = max(dp_with_last, ret)

        return ret
