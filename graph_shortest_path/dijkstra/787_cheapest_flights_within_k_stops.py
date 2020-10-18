# [Dijkstra, Shortest-Path, Classic]
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 787. Cheapest Flights Within K Stops

# History:
# Facebook, Airbnb
# 1.
# May 12, 2019
# 2.
# Jan 29, 2020
# 3.
# Oct 17, 2020

# There are n cities connected by m flights. Each fight starts from city u
# and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and
# the destination dst, your task is to find the cheapest price from src to
# dst with up to k stops. If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200,
# as marked red in the picture.
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500,
# as marked blue in the picture.
# Note:
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0
# to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
from heapq import heappop, heappush
from collections import defaultdict


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flight_route_prices = defaultdict(dict)

        for frm, to, price in flights:
            flight_route_prices[frm][to] = price

        hp = [[0, src, K]]

        while hp:
            cost, city, k_left = heappop(hp)

            if city == dst:
                return cost

            if k_left >= 0:
                for nxt_city, price in flight_route_prices[city].iteritems():
                    heappush(hp, [cost + price, nxt_city, k_left - 1])

        return -1
