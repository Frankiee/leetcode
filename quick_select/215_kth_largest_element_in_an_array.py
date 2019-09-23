# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array

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


class Solution(object):
    def partition(self, nums, l, r):
        pivot = nums[r]

        for curr in range(l, r):
            if nums[curr] < pivot:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1
        nums[l], nums[r] = nums[r], nums[l]
        return l

    def find_kth_smallest(self, nums, k, l, r):
        pivot_idx = self.partition(nums, l, r)

        if pivot_idx == k:
            return nums[k]
        elif pivot_idx > k:
            return self.find_kth_smallest(nums, k, l, r - 1)
        else:
            return self.find_kth_smallest(nums, k, l + 1, r)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        return self.find_kth_smallest(nums, len(nums) - k, 0, len(nums) - 1)
