# [Important]
# https://leetcode.com/problems/burst-balloons/
# 312. Burst Balloons

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After
# the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you
# can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5     +  3*5*8    +   1*3*8      + 1*8*1  = 167


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        dp = [[float('-inf')] * size for i in range(size)]

        for length in range(1, size + 1):
            for start in range(0, size - length + 1):
                end = start + length - 1
                for i in range(start, end + 1):
                    current = 0
                    # left
                    if start <= i - 1:
                        current += dp[start][i - 1]
                    # current
                    left = 1 if start < 1 else nums[start - 1]
                    center = nums[i]
                    right = 1 if end + 1 >= size else nums[end + 1]
                    current += left * center * right
                    # right
                    if i + 1 <= end:
                        current += dp[i + 1][end]
                    dp[start][end] = max(dp[start][end], current)

        return dp[0][size - 1]
