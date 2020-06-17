# [Classic]
# https://leetcode.com/problems/wiggle-sort-ii/
# 324. Wiggle Sort II

# History:
# TikTok
# 1.
# Apr 26, 2020

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?


class SolutionQuickSelect(object):
    def findKthSmallest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)

        return self._find_kth_smallest(nums, k - 1, 0, len(nums) - 1)

    def _find_kth_smallest(self, nums, k, l, r):
        p = self.partition(nums, l, r)

        if p == k:
            return nums[p]
        elif p > k:
            return self._find_kth_smallest(nums, k, l, p - 1)
        else:
            return self._find_kth_smallest(nums, k, p + 1, r)

    def partition(self, nums, l, r):
        pivot = nums[r]

        for curr in range(l, r):
            if nums[curr] < pivot:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1

        nums[l], nums[r] = nums[r], nums[l]

        return l

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = nums[::]

        self.findKthSmallest(temp, (len(temp) + 1) / 2)

        for i in range(1, len(nums), 2):
            nums[i] = temp.pop()

        for i in range(0, len(nums), 2):
            nums[i] = temp.pop()


# Better Solution Exists
class SolutionSort(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums[::])

        for i in range(1, len(nums), 2):
            nums[i] = temp.pop()

        for i in range(0, len(nums), 2):
            nums[i] = temp.pop()
