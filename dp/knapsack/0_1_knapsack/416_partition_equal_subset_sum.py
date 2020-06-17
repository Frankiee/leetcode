# [Classic, 0-1-Knapsack, Knapsack]
# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum

# Related:
# 698. Partition to K Equal Sum Subsets

# History:
# Facebook
# 1.
# May 18, 2019
# 2.
# Dec 16, 2019
# 3.
# Mar 22, 2020
# 4.
# May 11, 2020

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


class SolutionDPWithSet(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total / 2

        values = set()

        for n in nums:
            new_values = copy.copy(values)
            new_values.add(n)

            for v in values:
                new_values.add(v + n)

            if target in new_values:
                return True

            values = new_values

        return False


class SolutionDP(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        target_sum = nums_sum / 2

        dp = [[None] * (len(nums) + 1) for _ in range(target_sum + 1)]

        for s in range(target_sum + 1):
            for num_idx in range(len(nums) + 1):
                if s == 0 and num_idx == 0:
                    dp[s][num_idx] = True
                elif s == 0 or num_idx == 0:
                    dp[s][num_idx] = False
                else:
                    dp[s][num_idx] = dp[s][num_idx - 1] or (
                        dp[s - nums[num_idx - 1]][num_idx - 1] if s - nums[
                            num_idx - 1] >= 0 else False)

        return dp[target_sum][-1]
