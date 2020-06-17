# [Greedy, Classic, Stack]
# https://leetcode.com/problems/create-maximum-number/
# 321. Create Maximum Number

# Related: 402. Remove K Digits

# Given two arrays of length m and n with digits 0-9 representing two
# numbers. Create the maximum number of length k <= m + n from digits of the
# two. The relative order of the digits from the same array must be
# preserved. Return an array of the k digits.
#
# Note: You should try to optimize your time and space complexity.
#
# Example 1:
#
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]
# Example 2:
#
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
# Example 3:
#
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]


class Solution(object):
    def max_number(self, nums, k):
        freedom = max(len(nums) - k, 0)
        ret = []

        for n in nums:
            while ret and ret[-1] < n and freedom > 0:
                ret.pop()
                freedom -= 1
            ret.append(n)

        if len(ret) > k:
            ret = ret[:k]

        return ret

    def merge(self, nums1, nums2):
        ret = []
        while nums1 and nums2:
            if nums1 > nums2:
                ret.append(nums1.pop(0))
            else:
                ret.append(nums2.pop(0))

        if not nums1:
            ret.extend(nums2)
        if not nums2:
            ret.extend(nums1)

        return ret

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_nums = None
        for nums1_dis in range(max(0, k - len(nums2)),
                               min(k + 1, len(nums1) + 1)):
            nums1_max = self.max_number(nums1, nums1_dis)
            nums2_max = self.max_number(nums2, k - nums1_dis)
            merged_nums = self.merge(nums1_max, nums2_max)

            if not max_nums or merged_nums > max_nums:
                max_nums = merged_nums

        return max_nums
