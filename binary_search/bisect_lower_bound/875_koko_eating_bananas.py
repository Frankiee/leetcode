# [Bisect-Lower-Bound]
# https://leetcode.com/problems/koko-eating-bananas/
# 875. Koko Eating Bananas

# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile
# has piles[i] bananas.  The guards have gone and will come back in H hours.
#
# Koko can decide her bananas-per-hour eating speed of K.  Each hour,
# she chooses some pile of bananas, and eats K bananas from that pile.  If
# the pile has less than K bananas, she eats all of them instead, and won't
# eat any more bananas during this hour.
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas
# before the guards come back.
#
# Return the minimum integer K such that she can eat all the bananas within
# H hours.
#
#
#
# Example 1:
#
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
#
#
# Note:
#
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

import math


class Solution(object):
    def _min_hours(self, piles, k):
        return sum([math.ceil(p / float(k)) for p in piles])

    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        l = 1
        r = max(piles) + 1

        while l < r:
            m = l + (r - l) / 2

            min_hours = self._min_hours(piles, m)

            if min_hours <= H:
                r = m
            else:
                l = m + 1

        return l
