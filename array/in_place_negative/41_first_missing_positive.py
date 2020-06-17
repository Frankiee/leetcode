# [In-Place-Negative, Classic]
# https://leetcode.com/problems/first-missing-positive/
# 41. First Missing Positive

# History:
# Facebook
# 1.
# Dec 1, 2019

# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n <= 0:
                nums[i] = float('inf')

        for i, n in enumerate(nums):
            val = abs(n)
            idx = val - 1
            if idx < len(nums):
                nums[idx] = -abs(nums[idx])

        for i, n in enumerate(nums):
            if n > 0:
                return i + 1

        return len(nums) + 1
