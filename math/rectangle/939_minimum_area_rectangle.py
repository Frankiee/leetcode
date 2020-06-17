# [Classic, Rectangle]
# https://leetcode.com/problems/minimum-area-rectangle/
# 939. Minimum Area Rectangle

# History:
# Facebook
# 1.
# Mar 6, 2020
# 2.
# May 4, 2020

# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from
# these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
#
#
# Example 1:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
# Note:
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points_set = set([tuple(p) for p in points])
        ret = float('inf')

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                        ret = min(ret, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))

        return ret if ret != float('inf') else 0
