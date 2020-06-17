# [2-Pointers-Opposite, Classic]
# https://leetcode.com/problems/valid-triangle-number/
# 611. Valid Triangle Number

# History:
# Facebook
# 1.
# Sep 15, 2019
# 2.
# Mar 18, 2020
# 3.
# May 15, 2020

# Given an array consists of non-negative integers, your task is to count
# the number of triplets chosen from the array that can make triangles if we
# take them as side lengths of a triangle.
#
# Example 1:
# Input: [2,2,3,4]
# Output: 3
#
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        ret = 0
        for r in range(2, len(nums)):
            l, m = 0, r - 1

            while l < m:
                if nums[l] + nums[m] > nums[r]:
                    ret += m - l
                    m -= 1
                else:
                    l += 1

        return ret
