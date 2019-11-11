# [Classic, Dijkstra, Shortest-Path]
# https://leetcode.com/problems/network-delay-time/
# 743. Network Delay Time

# # History:
# # 1.
# # Nov 11, 2019

# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the
# source node, v is the target node, and w is the time it takes for a signal to travel from
# source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the
# signal? If it is impossible, return -1.
#
# Example 1:
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

import collections
import heapq


# 456 ms 14.2 MB
class SolutionDijkstra(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for s, e, t in times:
            graph[s].append((e, t))

        pq = [(0, K)]
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)

            if node in dist:
                continue

            dist[node] = d

            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        if any([n not in dist for n in range(1, N + 1)]):
            return -1
        else:
            return max(dist.values())
