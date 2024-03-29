# [In-Place-Negative]
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array

# History:
# Facebook
# 1.
# Mar 19, 2020

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice
# and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does
# not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])

        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)

        return ret
