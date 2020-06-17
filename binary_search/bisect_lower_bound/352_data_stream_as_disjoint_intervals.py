# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# 352. Data Stream as Disjoint Intervals

# History:
# Facebook
# 1.
# Mar 26, 2020
# 2.
# May 12, 2020

# Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers
# seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary
# will be:
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
#
# Follow up:
#
# What if there are lots of merges and the number of disjoint intervals are small compared to the
# data stream's size?


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def _bisect(self, val):
        l, r = 0, len(self.intervals)

        while l < r:
            m = (r - l) / 2 + l

            if self.intervals[m][1] >= val:
                r = m
            else:
                l = m + 1

        return l

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        pos = self._bisect(val)

        if 0 < pos < len(self.intervals):
            if self.intervals[pos - 1][1] + 1 == val == self.intervals[pos][0] - 1:
                self.intervals[pos - 1][1] = self.intervals[pos][1]
                self.intervals.pop(pos)

                return

        if 0 < pos:
            if self.intervals[pos - 1][1] + 1 == val:
                self.intervals[pos - 1][1] = val
                return

        if pos < len(self.intervals):
            if val == self.intervals[pos][0] - 1:
                self.intervals[pos][0] = val
            elif val < self.intervals[pos][0]:
                self.intervals.insert(pos, [val, val])
        else:
            self.intervals.insert(pos, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
