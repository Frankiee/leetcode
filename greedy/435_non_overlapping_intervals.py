# [Greedy]
# https://leetcode.com/problems/non-overlapping-intervals/
# 435. Non-overlapping Intervals

# History:
# 1.
# Apr 30, 2019
# 2.
# Nov 12, 2019
# 3.
# May 3, 2020

# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
#
# Note:
#
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't
# overlap each other.
#
#
# Example 1:
#
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
#
#
# Example 2:
#
# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
#
#
# Example 3:
#
# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda i: i[1])

        ret = 0
        pre_end = float('-inf')
        for s, e in intervals:
            if s >= pre_end:
                pre_end = e
            else:
                ret += 1

        return ret
