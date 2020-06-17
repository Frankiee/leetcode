# https://leetcode.com/problems/intersection-of-two-arrays/
# 349. Intersection of Two Arrays

# History:
# Facebook
# 1.
# May 2, 2020

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            to_loop, to_set = nums1, nums2
        else:
            to_loop, to_set = nums2, nums1

        num_set = set(to_set)

        ret = []
        for i in to_loop:
            if i in num_set:
                ret.append(i)
                num_set.remove(i)

        return ret
