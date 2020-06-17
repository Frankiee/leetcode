# [Classic]
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# 540. Single Element in a Sorted Array

# History:
# Facebook
# 1.
# Dec 15, 2019
# 2.
# Apr 30, 2020

# You are given a sorted array consisting of only integers where every element appears exactly
# twice, except for one element which appears exactly once. Find this single element that appears
# only once.
#
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if m % 2 == 1:
                m -= 1

            if m + 1 < len(nums) and nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        return nums[l]


class SolutionXOR(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0

        for n in nums:
            ret ^= n

        return ret
