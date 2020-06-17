# [Archived]
# https://leetcode.com/problems/zigzag-iterator/
# 281. Zigzag Iterator

# History:
# Facebook
# 1.
# Mar 7, 2020

# Given two 1d vectors, implement an iterator to return their elements alternately.
#
#
#
# Example:
#
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1,3,2,4,5,6].
#
#
# Follow up:
#
# What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does
# not look right to you, replace "Zigzag" with "Cyclic". For example:
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.v1_pt = 0
        self.v2_pt = 0
        self.ct = 0

    def next(self):
        """
        :rtype: int
        """
        if (self.ct % 2 == 0 or self.v2_pt >= len(self.v2)) and self.v1_pt < len(self.v1):
            ret = self.v1[self.v1_pt]
            self.v1_pt += 1
        else:
            ret = self.v2[self.v2_pt]
            self.v2_pt += 1

        self.ct += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return not (self.v1_pt >= len(self.v1) and self.v2_pt >= len(self.v2))

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
