# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array

# History:
# Netflix
# 1.
# May 5, 2020

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m
            else:
                return nums[l]

        return nums[l]
