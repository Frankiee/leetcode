# [Prefix-Sum]
# https://leetcode.com/problems/range-sum-query-immutable/
# 303. Range Sum Query - Immutable

# History:
# Facebook
# 1.
# Mar 24, 2020
# 2.
# May 5, 2020

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j),
# inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = nums

        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] += self.prefix_sum[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j] - self.prefix_sum[i - 1] if i > 0 else self.prefix_sum[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
