# [Important]
# https://leetcode.com/problems/sliding-window-maximum/description/
# 239. Sliding Window Maximum

# Given an array nums, there is a sliding window of size k which is moving
# from the very left of the array to the very right. You can only see the k
# numbers in the window. Each time the sliding window moves right by one
# position. Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 <= k <= input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?


class Solution(object):
    def __init__(self):
        self.sliding_window_max = []

    def build_sliding_window(self, idx):
        for i in range(len(self.sliding_window_max) - 1, -1, -1):
            if self.nums[self.sliding_window_max[i]] <= self.nums[idx]:
                self.sliding_window_max.pop()
            else:
                break

        self.sliding_window_max.append(idx)

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        self.nums = nums

        for i in range(0, k):
            self.build_sliding_window(i)

        ret = []
        ret.append(self.nums[self.sliding_window_max[0]])

        for i in range(k, len(self.nums)):
            self.build_sliding_window(i)
            if i - k == self.sliding_window_max[0]:
                self.sliding_window_max.pop(0)
            ret.append(self.nums[self.sliding_window_max[0]])

        return ret
