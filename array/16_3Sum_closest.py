# [Important, 2Sum]
# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

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
    def __init__(self, ):
        self.cloest_sum = None

    def assign_cloest_sum(self, new_sum, target):
        if new_sum == target:
            return True

        if self.cloest_sum is None:
            self.cloest_sum = new_sum
        elif abs(self.cloest_sum - target) > abs(new_sum - target):
            self.cloest_sum = new_sum

        return False

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 2):
            first_three_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if first_three_sum > target:
                if self.assign_cloest_sum(first_three_sum, target) is True:
                    return target
                break
            first_last_two_sum = nums[i] + nums[-1] + nums[-2]
            if first_last_two_sum < target:
                if self.assign_cloest_sum(first_last_two_sum, target) is True:
                    return target
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if self.assign_cloest_sum(current_sum, target) is True:
                    return target
                elif current_sum > target:
                    r -= 1
                else:
                    l += 1

        return self.cloest_sum
