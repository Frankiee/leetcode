# [Greedy, Classic, Time-Series]
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 452. Minimum Number of Arrows to Burst Balloons

# History:
# Facebook
# 1.
# Jun 13, 2019
# 2.
# Mar 27, 2020

# There are a number of spherical balloons spread in two-dimensional space.
# For each balloon, provided input is the start and end coordinates of the
# horizontal diameter. Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice. Start is
# always smaller than end. There will be at most 104 balloons.
#
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if
# xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be
# shot. An arrow once shot keeps travelling up infinitely. The problem is to
# find the minimum number of arrows that must be shot to burst all balloons.
#
# Example:
#
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda p: p[1])

        ret = 0
        last_burst_point = None
        for p in points:
            if last_burst_point is None or last_burst_point < p[0]:
                last_burst_point = p[1]
                ret += 1

        return ret


class SolutionInterval(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        ret = 1

        points.sort()

        overlap = points[0]

        for i in range(1, len(points)):
            nxt_point = points[i]

            if overlap[1] >= nxt_point[0]:
                overlap[0] = nxt_point[0]
                overlap[1] = min(overlap[1], nxt_point[1])
            else:
                overlap = points[i]
                ret += 1

        return ret
