# [Hard, XOR]
# https://leetcode.com/problems/single-number-iii/
# 260. Single Number III

# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two
# elements that appear only once.
#
# Example:
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:
#
# The order of the result is not important. So in the above example, [5,
# 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant space complexity?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n

        # mask to partition the a and b into two groups
        mask = 1
        while xor & mask == 0:
            mask <<= 1

        a = b = 0
        for n in nums:
            if mask & n == 0:
                a ^= n
            else:
                b ^= n

        return [a, b]
