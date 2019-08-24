# [2Sum]
# https://leetcode.com/problems/3sum/
# 15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the
# sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        ret = []

        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l + 1 < r and l > 0 and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while (r - 1 > l and
                           r + 1 < len(nums) and
                           nums[r] == nums[r + 1]):
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return ret
