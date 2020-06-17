# [DP-Array-Subarray]
# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

# History:
# 1.
# Apr 22, 2019
# 2.
# Nov 23, 2019
# 3.
# Nov 24, 2019
# Daily Interview Pro - Twitter

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
        ret = float('-inf')
        max_with_last = float('-inf')

        for n in nums:
            max_with_last = max(
                n,
                n + max_with_last
            )
            ret = max(ret, max_with_last)

        return ret


class SolutionPrefixSum(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        lowest = 0

        ret = float('-inf')
        for n in nums:
            ret = max(ret, n - lowest)
            lowest = min(lowest, n)

        return ret
