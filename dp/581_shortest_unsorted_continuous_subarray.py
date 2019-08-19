# [Important]
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
# 581. Shortest Unsorted Continuous Subarray

# Given an integer array, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will
# be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
# the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        max_unsorted = None
        max_so_far = float('-inf')

        for i, n in enumerate(nums):
            if max_so_far > n:
                max_unsorted = i
            max_so_far = max(max_so_far, n)

        min_unsorted = None
        min_so_far = float('inf')

        for i in range(len(nums) - 1, -1, -1):
            if min_so_far < nums[i]:
                min_unsorted = i
            min_so_far = min(min_so_far, nums[i])

        if max_unsorted is None or min_unsorted is None:
            return 0
        return max_unsorted - min_unsorted + 1
