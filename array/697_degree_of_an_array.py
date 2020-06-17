# https://leetcode.com/problems/degree-of-an-array/
# 697. Degree of an Array

# History:
# Robinhood
# 1.
# Feb 8, 2020

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as
# the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has
# the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = float('inf')
        degree = 0
        first_time = {}
        counter = {}

        for i, n in enumerate(nums):
            if n not in first_time:
                first_time[n] = i
                counter[n] = 1
            else:
                counter[n] += 1

            if counter[n] > degree:
                ret = i - first_time[n] + 1
            elif counter[n] == degree:
                ret = min(ret, i - first_time[n] + 1)

            degree = max(degree, counter[n])

        return ret
