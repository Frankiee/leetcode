# [Archived]
# https://leetcode.com/problems/two-sum/
# 1. Two Sum

# History:
# Google, Facebook
# 1.
# Aug 21, 2019
# 2.
# Mar 10, 2020
# 3.
# May 2, 2020

# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dp = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in dp:
                return [dp[diff], i]
            dp[n] = i

        return None
