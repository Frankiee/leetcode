# [In-Place-Swap, Classic]
# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors

# History:
# Facebook
# 1.
# Jan 9, 2020
# 2.
# Mar 29, 2020
# 3.
# Apr 30, 2020

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of
# the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
# respectively.
#55
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total
# number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_idx, white_idx, blue_idx = 0, 0, len(nums) - 1

        while white_idx <= blue_idx:
            color = nums[white_idx]
            if color == 1:
                white_idx += 1
            elif color == 0:
                nums[white_idx], nums[red_idx] = nums[red_idx], nums[white_idx]
                red_idx += 1
                white_idx += 1
            else:
                nums[white_idx], nums[blue_idx] = nums[blue_idx], nums[white_idx]
                blue_idx -= 1
