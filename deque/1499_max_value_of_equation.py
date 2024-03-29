# [Classic]
# https://leetcode.com/problems/max-value-of-equation/
# 1499. Max Value of Equation

# History:
# Google
# 1.
# Aug 1, 2020

# Given an array points containing the coordinates of points on a 2D plane, sorted by the
# x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You
# are also given an integer k.
#
# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j
# <= points.length. It is guaranteed that there exists at least one pair of points that satisfy
# the constraint |xi - xj| <= k.
#
#
#
# Example 1:
#
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the
# equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and
# give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
# Example 2:
#
# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or less in the
# x-values, and give the value of 0 + 0 + |0 - 3| = 3.
#
#
# Constraints:
#
# 2 <= points.length <= 10^5
# points[i].length == 2
# -10^8 <= points[i][0], points[i][1] <= 10^8
# 0 <= k <= 2 * 10^8
# points[i][0] < points[j][0] for all 1 <= i < j <= points.length
# xi form a strictly increasing sequence.


from collections import deque


class SolutionDeque(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # yi + yj + |xi - xj| = yi + yj - xi + xj = (yi - xi) + (xj + yj)
        deq = deque()

        ret = float('-inf')
        for x, y in points:
            while deq and x - deq[0][1] > k:
                deq.popleft()

            if deq:
                ret = max(ret, deq[0][0] + x + y)

            while deq and deq[-1][0] < y - x:
                deq.pop()

            deq.append((y - x, x))

        return ret


from heapq import heappop, heappush


# Time O(NlogN)
# Space O(N)
class SolutionPrirotyQueue(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # yi + yj + |xi - xj| = yi + yj - xi + xj = (yi - xi) + (xj + yj)
        hp = []
        ret = float('-inf')
        for x, y in points:
            while hp and x - hp[0][1] > k:
                heappop(hp)

            if hp:
                ret = max(ret, -hp[0][0] + x + y)

            heappush(hp, (x - y, x))

        return ret
