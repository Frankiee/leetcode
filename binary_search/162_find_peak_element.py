# https://leetcode.com/problems/find-peak-element/
# 162. Find Peak Element

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

        l = 1
        r = len(nums) + 1

        while l < r:
            m = l + (r - l) / 2

            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m - 1
            if nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m

        if 0 < m < len(nums) + 1:
            return l - 1

        return -1
