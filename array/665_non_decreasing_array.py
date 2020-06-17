# [Classic]
# https://leetcode.com/problems/non-decreasing-array/
# 665. Non-decreasing Array

# History:
# Google
# 1.
# Mar 10, 2020
# 2.
# Jun 15, 2020

# Given an array with n integers, your task is to check if it could become non-decreasing by
# modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        count_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_dec += 1

                if count_dec >= 2:
                    return False

                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]

        return True
