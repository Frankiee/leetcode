# [Classic, 0-1-Knapsack, Knapsack]
# https://leetcode.com/problems/target-sum/
# 494. Target Sum

# History:
# Facebook
# 1.
# May 20, 2019
# 2.
# Nov 13, 2019
# 3.
# Mar 22, 2020

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


from collections import defaultdict


class SolutionDPReverseCheck(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)

        if total < S:
            return 0

        dp = defaultdict(int)
        dp[total] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for s, ways in dp.iteritems():
                new_dp[s + nums[i]] += ways
                new_dp[s - nums[i]] += ways

            dp = new_dp

        return dp[total + S]


class SolutionDP(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)

        if total < S:
            return 0

        dp = [0] * (2 * total + 1)
        dp[total] = 1

        for i in range(len(nums)):
            new_dp = [0] * (2 * total + 1)
            for s in range(2 * total + 1):
                new_dp[s] += dp[s - nums[i]] if s - nums[i] >= 0 else 0
                new_dp[s] += dp[s + nums[i]] if s + nums[i] < (2 * total + 1) else 0

            dp = new_dp

        return dp[total + S]


from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        max_num = sum(nums)
        if S > max_num and S < - max_num:
            return 0

        current_count = defaultdict(int)
        previous_count = defaultdict(int)

        for i in range(len(nums)):
            if i == 0:
                current_count[nums[0]] += 1
                current_count[-nums[0]] += 1
            else:
                for val, count in previous_count.iteritems():
                    current_count[val + nums[i]] += count
                    current_count[val - nums[i]] += count

            previous_count = current_count
            current_count = defaultdict(int)

        return previous_count[S]
