# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# 442. Find All Duplicates in an Array

# History:
# Facebook
# 1.
# Feb 11, 2019
# 2.
# Nov 17, 2019
# 3.
# May 5, 2020

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []

        for n in nums:
            if nums[abs(n) - 1] < 0:
                ret.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1

        return ret
