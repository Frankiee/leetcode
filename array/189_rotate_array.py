# [Classic]
# https://leetcode.com/problems/rotate-array/
# 189. Rotate Array

# History:
# Apple
# 1.
# Mar 31, 2020

# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this
# problem.
# Could you do it in-place with O(1) extra space?


class Solution(object):
    def _reverse(self, nums, l, r):
        for i in range((r - l + 1) / 2):
            nums[l + i], nums[r - i] = nums[r - i], nums[l + i]

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        self._reverse(nums, 0, len(nums) - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, len(nums) - 1)
