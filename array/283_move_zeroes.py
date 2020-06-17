# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes

# History:
# Facebook
# 1.
# Dec 9, 2019
# 2.
# Apr 13, 2020
# 3.
# Apr 22, 2020

# Given an array nums, write a function to move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for idx, curr in enumerate(nums):
            if curr != 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                l += 1

        for i in range(l, len(nums)):
            nums[i] = 0
