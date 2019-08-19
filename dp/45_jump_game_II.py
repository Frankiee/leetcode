# [Important]
# https://leetcode.com/problems/jump-game-ii/description/
# 45. Jump Game II

# Given an array of non-negative integers, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        step = 1
        current_max = nums[0]
        next_max = float('-inf')

        for i in range(len(nums)):
            if i > current_max:
                step += 1
                current_max = next_max
                next_max = float('-inf')
            next_max = max(next_max, i + nums[i])

        return step
