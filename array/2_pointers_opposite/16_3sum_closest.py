# [2-Pointers-Opposite]
# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# History:
# Facebook
# 1.
# Aug 21, 2019
# 2.
# Feb 02, 2020
# 3.
# Apr 4, 2020
# 4.
# May 12, 2020

# Given an array nums of n integers and an integer target, find three
# integers in nums such that the sum is closest to target. Return the sum of
# the three integers. You may assume that each input would have exactly one
# solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        ret = float('inf')
        for l in range(len(nums) - 2):
            total = nums[l] + nums[l + 1] + nums[l + 2]
            if total == target:
                return target
            if abs(total - target) < abs(ret - target):
                ret = total
            if total >= target:
                break

            total = nums[l] + nums[-1] + nums[-2]
            if total == target:
                return target
            if abs(total - target) < abs(ret - target):
                ret = total
            if total <= target:
                continue

            m, r = l + 1, len(nums) - 1

            while m < r:
                total = nums[l] + nums[m] + nums[r]

                if total == target:
                    return target
                if abs(total - target) < abs(ret - target):
                    ret = total

                if total < target:
                    m += 1
                else:
                    r -= 1

        return ret
