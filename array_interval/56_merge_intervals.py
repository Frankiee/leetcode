# [Important]
# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals

# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []

        intervals = sorted(intervals, key=lambda i: i[0])

        current_next = None

        for i in intervals:
            if not current_next:
                current_next = i
            elif i[0] > current_next[1]:
                ret.append(current_next)
                current_next = i
            else:
                current_next = [
                    min(current_next[0], i[0]),
                    max(current_next[1], i[1]),
                ]

        if current_next:
            ret.append(current_next)

        return ret
