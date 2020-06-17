# https://leetcode.com/problems/find-peak-element/
# 162. Find Peak Element

# History:
# Facebook
# 1.
# Dec 20, 2019
# 2.
# Feb 20, 2020
# 3.
# Apr 3, 2020
# 4.
# Apr 7, 2020
# 5.
# May 5, 2020

# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element
# and return its index.
#
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2,
#              or index number 5 where the peak element is 6.
# Note:
#
# Your solution should be in logarithmic complexity.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))

        l, r = 1, len(nums) - 1

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                return m - 1
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l - 1
