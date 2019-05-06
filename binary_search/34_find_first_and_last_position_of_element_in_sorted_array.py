# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/  # nopa
# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution(object):
    def lower_bound(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) / 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if 0 <= l < len(nums) and nums[l] == target:
            return l
        return -1

    def upper_bound(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) / 2

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        if 0 < l <= len(nums) and nums[l - 1] == target:
            return l - 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.lower_bound(nums, target), self.upper_bound(nums, target)]
