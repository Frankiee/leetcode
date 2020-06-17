# [Bisect-Lower-Bound]
# https://leetcode.com/problems/sliding-window-median/
# 480. Sliding Window Median

# History:
# Facebook
# 1.
# May 12, 2020

# Median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the
# sliding window moves right by one position. Your job is to output the median array for each
# window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's size for non-empty
# array.
# Answers within 10^-5 of the actual value will be accepted as correct.


class Solution(object):
    def _bisect_lower(self, lst, i):
        l, r = 0, len(lst)

        while l < r:
            m = (r - l) / 2 + l

            if lst[m] >= i:
                r = m
            else:
                l = m + 1

        return l

    def _get_medium(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) / 2]

        return (nums[len(nums) / 2] + nums[len(nums) / 2 - 1]) / float(2)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        buff = []
        for i in range(k):
            pos = self._bisect_lower(buff, nums[i])
            buff.insert(pos, nums[i])

        ret = []
        ret.append(self._get_medium(buff))

        for i in range(k, len(nums)):
            pos = self._bisect_lower(buff, nums[i - k])
            buff.pop(pos)
            pos = self._bisect_lower(buff, nums[i])
            buff.insert(pos, nums[i])

            ret.append(self._get_medium(buff))

        return ret
