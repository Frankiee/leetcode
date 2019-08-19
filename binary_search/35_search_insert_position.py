# [Important]
# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position

# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        l_idx, r_idx = 0, len(nums) - 1

        if target <= nums[l_idx]:
            return 0
        if target > nums[r_idx]:
            return r_idx + 1

        while l_idx <= r_idx:
            mid = (l_idx + r_idx) / 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r_idx = mid - 1
            elif nums[mid] < target:
                l_idx = mid + 1

        return l_idx
