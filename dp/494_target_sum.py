# https://leetcode.com/problems/target-sum/
# 494. Target Sum

# You are given a list of non-negative integers, a1, a2, ..., an,
# and a target, S. Now you have 2 symbols + and -. For each integer,
# you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        highest = sum(nums)

        if S > highest:
            return 0

        dp = [None] * len(nums)
        for row in range(len(dp)):
            dp[row] = [0] * (2 * highest + 1)

        for i in range(len(dp)):
            for s in range(2 * highest + 1):
                s_value = s - highest
                if i == 0:
                    if s_value == nums[0]:
                        dp[i][s] += 1
                    if s_value == -nums[0]:
                        dp[i][s] += 1
                else:
                    if highest >= s_value - nums[i] >= -highest:
                        dp[i][s] += dp[i - 1][s - nums[i]]
                    if highest >= s_value + nums[i] >= -highest:
                        dp[i][s] += dp[i - 1][s + nums[i]]

        return dp[len(nums) - 1][S + highest]
