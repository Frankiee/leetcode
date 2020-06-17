# https://leetcode.com/problems/interval-list-intersections/
# 986. Interval List Intersections

# History:
# Facebook
# 1.
# Dec 8, 2019
# 2.
# Mar 29, 2020
# 3.
# Apr 10, 2020
# 4.
# May 2, 2020

# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted
# order.
#
# Return the intersection of56 these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x
# <= b.  The intersection of two closed intervals is a set of real numbers that is either empty,
# or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2,
# 4] is [2, 3].)
#
#
#
# Example 1:
#
#
#
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or
# lists.
#
#
# Note:
#
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9


class Solution1(object):
    def _get_intersection(self, item1, item2):
        max_start = max(item1[0], item2[0])
        min_end = min(item1[1], item2[1])

        if max_start <= min_end:
            return [max_start, min_end]

        return None

    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        a_p = b_p = 0

        while a_p < len(A) and b_p < len(B):
            nxt = self._get_intersection(A[a_p], B[b_p])

            if nxt:
                ret.append(nxt)

            if A[a_p][1] < B[b_p][1]:
                a_p += 1
            elif A[a_p][1] > B[b_p][1]:
                b_p += 1
            else:
                a_p += 1
                b_p += 1

        return ret


class Solution2(object):
    def _get_intersection(self, interval1, interval2):
        max_s = max(interval1[0], interval2[0])
        min_e = min(interval1[1], interval2[1])

        if max_s > min_e:
            return None

        return [max_s, min_e]

    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        a_i, b_i = 0, 0

        while a_i < len(A) and b_i < len(B):
            interval1, interval2 = A[a_i], B[b_i]
            intersection = self._get_intersection(interval1, interval2)

            if intersection:
                ret.append(intersection)

            if interval1[1] > interval2[1]:
                b_i += 1
            else:
                a_i += 1

        return ret
