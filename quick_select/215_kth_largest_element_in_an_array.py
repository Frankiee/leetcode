# [Quick-Select, Classic]
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array

# History:
# Facebook
# 1.
# Apr 1, 2019
# 2.
# Nov 21, 2019
# 3.
# Mar 31, 2020
# 4.
# Apr 22, 2020

# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


# Quick Select
# Also refer to the Min Heap solution
# https://www.youtube.com/watch?v=zyskis1Gw0c
import random


class SolutionGreater(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)

        return self._find_kth_largest(nums, k - 1, 0, len(nums) - 1)

    def _find_kth_largest(self, nums, k, l, r):
        p = self.partition(nums, l, r)

        if p == k:
            return nums[p]
        elif p > k:
            return self._find_kth_largest(nums, k, l, p - 1)
        else:
            return self._find_kth_largest(nums, k, p + 1, r)

    def partition(self, nums, l, r):
        pivot = nums[r]

        for curr in range(l, r):
            if nums[curr] > pivot:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1

        nums[l], nums[r] = nums[r], nums[l]

        return l


class SolutionGreaterEqual(object):
    def _partition(self, nums, l, r):
        pivot = nums[r]

        for curr in range(l, r):
            if nums[curr] >= pivot:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1

        nums[r], nums[l] = nums[l], nums[r]

        return l

    def _find_kth_largest(self, nums, k, l, r):
        pos = self._partition(nums, l, r)

        if pos == k:
            return nums[pos]
        elif pos > k:
            return self._find_kth_largest(nums, k, l, pos - 1)
        else:
            return self._find_kth_largest(nums, k, pos + 1, r)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        return self._find_kth_largest(nums, k - 1, 0, len(nums) - 1)
