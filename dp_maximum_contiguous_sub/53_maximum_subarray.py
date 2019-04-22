# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

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
        current_dp = float('-inf')
        max_so_far = float('-inf')

        for i in nums:
            current_dp = i if current_dp < 0 else current_dp + i
            max_so_far = max(max_so_far, current_dp)

        return max_so_far
