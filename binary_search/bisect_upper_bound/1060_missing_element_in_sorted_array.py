# [Bisect-Upper-Bound, Classic]
# https://leetcode.com/problems/missing-element-in-sorted-array/
# 1060. Missing Element in Sorted Array

# History:
# Facebook
# 1.
# Dec 14, 2019
# 2.
# Apr 13, 2020
# 3.
# Apr 28, 2020

# Given a sorted array A of unique numbers, find the K-th missing number starting from the
# leftmost number of the array.
#
#
#
# Example 1:
#
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation:
# The first missing number is 5.
# Example 2:
#
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation:
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# Example 3:
#
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation:
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
#
#
# Note:
#
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            missing = (nums[m] - nums[0]) - m

            if missing >= k:
                r = m
            else:
                l = m + 1

#        return nums[l - 1] + k - (nums[l - 1] - nums[0]) + l - 1
        return nums[0] + k + l - 1


class SolutionDoubleBinarySearch(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = nums[0], 1000000001

        while l < r:
            m = (r - l) / 2 + l

            pos = bisect.bisect_right(nums, m)
            missing_count = m - nums[0] - pos + 1

            if missing_count >= k:
                r = m
            else:
                l = m + 1

        return l


class SolutionDeprecated(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] - 1 >= k:
                return nums[i] + k
            else:
                k -= (nums[i + 1] - nums[i] - 1)

        return nums[-1] + k
