# [Bitwise, Classic]
# https://leetcode.com/problems/single-number-ii/
# 137. Single Number II

# https://leetcode.com/problems/single-number-ii/

# History:
# Facebook
# 1.
# Aug 24, 2019
# 2.
# Apr 28, 2020

# Given a non-empty array of integers, every element appears three times
# except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,3,2]
# Output: 3
# Example 2:
#
# Input: [0,1,0,1,0,1,99]
# Output: 99


class Solution(object):
    def _convert(self, x):
        # In python if you has a positive integer, you can't get negative integer by setting its
        # highest bit to 1 because there is no highest bit actually. Int in python is an object
        # and has no upper limit, you could try 1<<31, you get 2147483648 other than -2147483648.
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0

        for i in range(32):
            count = 0

            for n in nums:
                if n >> i & 1 == 1:
                    count += 1
                    count %= 3

            if count != 0:
                ret |= (1 << i)

        return self._convert(ret)


class SolutionDeprecated(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)
        nums_unique_sum = sum(set(nums))

        return nums_sum - (nums_sum - nums_unique_sum) / 2 * 3
