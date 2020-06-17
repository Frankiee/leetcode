# [In-Place-Negative]
# https://leetcode.com/problems/missing-number/
# 268. Missing Number

# History:
# Apple
# 1.
# Mar 20, 2020
# 2.
# Apr 13, 2020

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is
# missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only
# constant extra space complexity?


class SolutionSum(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (0 + len(nums)) * (len(nums) + 1) / 2

        return total - sum(nums)


class SolutionDeprecated(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num_seen = False

        for i in range(len(nums)):
            if abs(nums[i]) != len(nums):
                nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
            else:
                max_num_seen = True

        zero_idx = None
        for i in range(len(nums)):
            if nums[i] > 0:
                return i

            if nums[i] == 0:
                zero_idx = i

        if not max_num_seen:
            return len(nums)

        return zero_idx
