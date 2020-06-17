# [Classic]
# https://leetcode.com/problems/game-of-life/
# 31. Next Permutation

# History:
# Facebook
# 1.
# Feb 4, 2020
# 2.
# Apr 6, 2020
# 3.
# May 15, 2020

# Implement next permutation, which rearranges numbers into the lexicographically next greater
# permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie,
# sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in
# the right-hand column.
#
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1


class SolutionBinarySearch(object):
    def _find_smallest_greater(self, i, start, nums):
        l, r = start, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] <= nums[i]:
                r = m
            else:
                l = m + 1
        return l - 1

    def _reverse(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                j = self._find_smallest_greater(i, i + 1, nums)
                nums[i], nums[j] = nums[j], nums[i]
                self._reverse(i + 1, len(nums) - 1, nums)
                return

        self._reverse(0, len(nums) - 1, nums)


class Solution(object):
    def _find_smallest_greater(self, nums, base, i):
        while i + 1 < len(nums) and nums[i + 1] > base:
            i += 1

        return i

    def _reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                j = self._find_smallest_greater(nums, nums[i], i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                self._reverse(nums, i + 1, len(nums) - 1)

                return

        self._reverse(nums, 0, len(nums) - 1)
