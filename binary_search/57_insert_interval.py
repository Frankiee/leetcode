# [bisect]
# https://leetcode.com/problems/insert-interval/
# 57. Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.


class Solution(object):
    def bisect(self, intervals, num, key):
        l = 0
        r = len(intervals)

        while l < r:
            m = l + (r - l) / 2

            if num > key(intervals[m]):
                l = m + 1
            elif num == key(intervals[m]):
                return m
            else:
                r = m

        return l

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        left_overlap = self.bisect(intervals, newInterval[0], lambda i: i[1])
        right_bisect = self.bisect(intervals, newInterval[1], lambda i: i[0])

        if (right_bisect < len(intervals) and
                intervals[right_bisect][0] == newInterval[1]):
            right_overlap = right_bisect
        else:
            right_overlap = right_bisect - 1

        ret = intervals[:left_overlap]
        ret.append([
            min(
                newInterval[0],
                intervals[left_overlap][0]
                if left_overlap is not None and
                   0 <= left_overlap < len(intervals) else float('inf')
            ),
            max(
                newInterval[1],
                intervals[right_overlap][1]
                if right_overlap is not None and
                   0 <= right_overlap < len(intervals) else float('-inf')
            )
        ])
        ret.extend(intervals[right_overlap+1:])

        return ret
