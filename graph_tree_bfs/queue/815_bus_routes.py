# [BFS, Queue]
# https://leetcode.com/problems/bus-routes/
# 815. Bus Routes

# We have a list of bus routes. Each routes[i] is a bus route that the i-th
# bus repeats forever. For example if routes[0] = [1, 5, 7], this means that
# the first bus (0-th indexed) travels in the sequence
# 1->5->7->1->5->7->1->... forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we
# must take to reach our destination? Return -1 if it is not possible.
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# Note:
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.


from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        if not routes:
            return -1

        stops = defaultdict(set)
        for i, buses in enumerate(routes):
            for b in buses:
                stops[b].add(i)

        # bus stop, steps
        to_visit = [(S, 0)]

        visited = {S}
        while to_visit:
            next_stop, step = to_visit.pop(0)

            if next_stop == T:
                return step

            connected_idxes = stops[next_stop]

            for connected_idx in connected_idxes:
                for b in routes[connected_idx]:
                    if b not in visited and next_stop != b:
                        visited.add(b)
                        to_visit.append((b, step + 1))

        return -1
