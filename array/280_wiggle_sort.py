# [Classic]
# https://leetcode.com/problems/wiggle-sort/
# 280. Wiggle Sort

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 25, 2020

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <=
# nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ascend = True

        for i in range(len(nums) - 1):
            if (ascend and nums[i] > nums[i + 1]) or (not ascend and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            ascend = not ascend
