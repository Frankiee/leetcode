# [Archived]
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167. Two Sum II - Input array is sorted

# History:
# Apple
# 1.
# Mar 21, 2020

# Given an array of integers that is already sorted in ascending order, find two numbers such
# that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the
# target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same
# element twice.
# Example:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
