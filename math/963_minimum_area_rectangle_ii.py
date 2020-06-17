# [Classic, Rectangle]
# https://leetcode.com/problems/minimum-area-rectangle-ii/
# 963. Minimum Area Rectangle II

# History:
# Facebook
# 1.
# Mar 6, 2020

# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from
# these points, with sides not necessarily parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
#
#
# Example 1:
#
#
#
# Input: [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
# Example 2:
#
#
#
# Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
# Example 3:
#
#
#
# Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
# Example 4:
#
#
#
# Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
#
#
# Note:
#
# 1 <= points.length <= 50
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# Answers within 10^-5 of the actual value will be accepted as correct.

from collections import defaultdict


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = [complex(*z) for z in points]
        points_indices = defaultdict(list)
        ret = float('inf')

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]

                center = (p1 + p2) / 2
                redius = abs(center - p1)

                points_indices[(center, redius)].append(p1)

        for (center, redius), groups in points_indices.iteritems():
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):
                    p1, p2 = groups[i], groups[j]
                    ret = min(ret, abs(p1 - p2) * abs(p1 - (2 * center - p2)))

        return ret if ret != float('inf') else 0
