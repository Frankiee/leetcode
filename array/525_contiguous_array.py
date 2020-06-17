# https://leetcode.com/problems/contiguous-array/description/
# 525. Contiguous Array

# History:
# 1.
# Feb 11, 2019
# 2.
# Nov 23, 2019

# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of
# 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {0: 0}

        curr_balance = 0
        max_balance = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_balance += 1
            else:
                curr_balance -= 1
            if curr_balance not in dp:
                dp[curr_balance] = i + 1
            else:
                max_balance = max(max_balance, i - dp[curr_balance] + 1)

        return max_balance
