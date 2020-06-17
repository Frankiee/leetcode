# [Classic]
# https://leetcode.com/problems/4sum/
# 18. 4Sum

# History:
# Facebook
# 1.
# Apr 12, 2020

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in
# nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the
# sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        two_sum = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum[nums[i] + nums[j]].append([i, j])

        ret = []
        for k1 in two_sum.keys():
            k2 = target - k1
            for p1 in two_sum[k1]:
                for p2 in two_sum[k2]:
                    if p1[1] < p2[0]:
                        cs = p1[:] + p2[:]
                        if all([i == 0 or
                                nums[i - 1] != nums[i] or
                                i - 1 in cs for i in cs]):
                            ret.append([nums[i] for i in cs])

        return ret
