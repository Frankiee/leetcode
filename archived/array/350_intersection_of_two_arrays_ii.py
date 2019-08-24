# [Archived]
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 350. Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited
# such that you cannot load all elements into the memory at once?


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        ret = []

        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return ret

        nums1_i = nums2_i = 0

        while nums1_i < len(nums1) and nums2_i < len(nums2):
            nums1_n = nums1[nums1_i]
            nums2_n = nums2[nums2_i]
            if nums1_n < nums2_n:
                nums1_i += 1
            elif nums1_n == nums2_n:
                ret.append(nums1_n)
                nums1_i += 1
                nums2_i += 1
            else:
                nums2_i += 1

        return ret
