# [2-Pointers-Cycle-Detection, Classic]
# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# Apr 30, 2020

# Given an array nums containing n + 1 integers where each integer is between 1 and n (
# inclusive), prove that at least one duplicate number must exist. Assume that there is only one
# duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        new = 0

        while True:
            slow = nums[slow]
            new = nums[new]

            if slow == new:
                return slow


class SolutionModifyArray(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if nums[abs(n)] < 0:
                return abs(n)
            nums[abs(n)] *= -1
