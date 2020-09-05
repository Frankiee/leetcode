# [Quick-Select, Classic]
# https://leetcode.com/problems/k-closest-points-to-origin/
# 973. K Closest Points to Origin

# History:
# Facebook, Google
# 1.
# Jun 14, 2019
# 2.
# Nov 21, 2019
# 3.
# Feb 21, 2020
# 4.
# Apr 22, 2020
# 5.
# May 12, 2020
# 6.
# Aug 1, 2020

# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
#
#
#
# Example 1:
#
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is
# just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)


# O(n) in average with quick select
import random


class SolutionQuickSelect(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        random.shuffle(points)

        return self._k_closest(points, K - 1, 0, len(points) - 1)

    def _k_closest(self, points, k, l, r):
        pos = self._partition(points, l, r)

        if pos == k:
            return points[:k + 1]
        elif pos > k:
            return self._k_closest(points, k, l, pos - 1)
        else:
            return self._k_closest(points, k, pos + 1, r)

    def _partition(self, points, l, r):
        pivot = points[r]
        pivot_distance = self._get_distance(pivot)

        for curr in range(l, r):
            if self._get_distance(points[curr]) < pivot_distance:
                points[curr], points[l] = points[l], points[curr]
                l += 1

        points[r], points[l] = points[l], points[r]

        return l

    def _get_distance(self, point):
        return point[0] ** 2 + point[1] ** 2


# O(log(n)) with max heap
from heapq import heappush, heappop


class SolutionMaxHeap(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        hp = []

        for p in points:
            heappush(hp, (-(p[0] ** 2 + p[1] ** 2), p))
            if len(hp) > K:
                heappop(hp)

        return [item[1] for item in hp]
