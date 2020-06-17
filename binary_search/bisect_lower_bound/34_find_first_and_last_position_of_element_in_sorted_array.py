# [Bisect-Lower-Bound]
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/  # nopa
# 34. Find First and Last Position of Element in Sorted Array

# History:
# Facebook, Netflix
# 1.
# May 6, 2019
# 2.
# Nov 23, 2019
# 3.
# Dec 18, 2019
# 4.
# Jun, 7, 2020

# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class SolutionBisect(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_pos = bisect.bisect_left(nums, target)

        if l_pos >= len(nums) or nums[l_pos] != target:
            return -1, -1

        r_pos = l_pos

        while r_pos + 1 < len(nums) and nums[r_pos + 1] == target:
            r_pos += 1

        return l_pos, r_pos


class SolutionLowerUpperBound(object):
    def _bisect_lower(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return l

    def _bisect_upper(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bl_pos = self._bisect_lower(nums, target)

        if bl_pos >= len(nums) or nums[bl_pos] != target:
            return -1, -1

        bu_pos = self._bisect_upper(nums, target)

        return bl_pos, bu_pos - 1


class SolutionOnlyLowerBound(object):
    def bisect(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) / 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bisect_left = self.bisect(nums, target)

        if bisect_left < 0 or bisect_left >= len(nums):
            return [-1, -1]
        if nums[bisect_left] != target:
            return [-1, -1]

        bisect_right = bisect_left
        while bisect_right < len(nums) - 1 and nums[bisect_right + 1] == target:
            bisect_right += 1

        return [bisect_left, bisect_right]
