# [Hard, 0-1-Knapsack]
# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum

# Related:
# 698. Partition to K Equal Sum Subsets

# Given a non-empty array containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total % 2 != 0:
            return False

        goal = total / 2

        # dp[i][j] represents if we can sum to j using first i numbers
        dp = [None] * len(nums)

        for num_idx in range(len(nums)):
            dp[num_idx] = [False] * (goal + 1)

        for num_idx in range(len(nums)):
            for s in range(goal + 1):
                if num_idx == 0:
                    if s == 0 or s == nums[0]:
                        dp[num_idx][s] = True
                else:
                    if dp[num_idx - 1][s]:
                        dp[num_idx][s] = True
                    elif (s - nums[num_idx] >= 0 and
                          dp[num_idx - 1][s - nums[num_idx]]):
                        dp[num_idx][s] = True

        return dp[len(nums) - 1][goal]
