# https://leetcode.com/problems/binary-search/
# 704. Binary Search

# https://www.youtube.com/watch?v=v57lNF2mb_s

# History:
# 1.
# May 6, 2019
# 2.
# Nov 20, 2019
# 3.
# Mar 7, 2020

# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Note:
#
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) / 2

            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return -1
