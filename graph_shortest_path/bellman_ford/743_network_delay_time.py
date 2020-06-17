# [Classic, Bellman-Ford, Shortest-Path]
# https://leetcode.com/problems/network-delay-time/
# 743. Network Delay Time

# History:
# 1.
# Nov 8, 2019

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


# 1696 ms 13.8 MB
class SolutionBellmanFord(object):
    MAX_REACHABLE_TIME = 101 * 100

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        max_times = [self.MAX_REACHABLE_TIME] * N
        max_times[K - 1] = 0

        for _ in range(N):
            for time_edge in times:
                start = time_edge[0] - 1
                end = time_edge[1] - 1
                time = time_edge[2]
                max_times[end] = min(max_times[end], max_times[start] + time)

        max_time = max(max_times)
        return -1 if max_time == self.MAX_REACHABLE_TIME else max_time
