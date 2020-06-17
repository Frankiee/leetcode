# [Classic]
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array

# History:
# Facebook
# 1.
# Feb 22, 2020
# 2.
# Mar 31, 2020
# 3.
# May 15, 2020

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise
# return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] == target:
                return m

            # rotation on the left half
            if nums[m] < nums[l]:
                if nums[m] < target <= nums[r - 1]:
                    l = m + 1
                else:
                    r = m
            # rotation on the right half
            elif nums[m] > nums[r - 1]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            # no rotation
            else:
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1

        return l if 0 <= l < len(nums) and nums[l] == target else -1
