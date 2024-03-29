# [XOR]
# https://leetcode.com/problems/single-number/
# 136. Single Number

# History:
# Facebook
# 1.
# Dec 15, 2019
# 2.
# Apr 28, 2020

# Given a non-empty array of integers, every element appears twice except
# for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0

        for n in nums:
            ret ^= n

        return ret
