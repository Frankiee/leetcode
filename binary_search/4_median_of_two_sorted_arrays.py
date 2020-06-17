# [Classic]
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 4. Median of Two Sorted Arrays

# History:
# Facebook
# 1.
# May 12, 2020

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


# Better solution exists
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)

        return (
            self._find_kth(nums1, nums2, total / 2)
            if total % 2 == 1 else
            (self._find_kth(nums1, nums2, total / 2) +
             self._find_kth(nums1, nums2, total / 2 - 1)) / 2.0
        )

    def _find_kth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            long_nums, short_nums = nums1, nums2
        else:
            long_nums, short_nums = nums2, nums1

        if len(short_nums) == 0:
            return long_nums[k]

        if k == len(long_nums) + len(short_nums) - 1:
            return max(long_nums[-1], short_nums[-1])

        i = len(short_nums) / 2
        j = k - i

        if short_nums[i] > long_nums[j]:
            return self._find_kth(short_nums[:i], long_nums[j:], i)
        else:
            return self._find_kth(short_nums[i:], long_nums[:j], j)
