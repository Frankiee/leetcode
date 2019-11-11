# Shortest Path Algorithms

## Bellman-Ford


## Floyd-Warshall


## Dijkstra
Single Source Shortest Path
Direct or undirected


### Example:

https://leetcode.com/problems/network-delay-time/
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the
source node, v is the target node, and w is the time it takes for a signal to travel from
source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the
signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:

* N will be in the range [1, 100].
* K will be in the range [1, N].
* The length of times will be in the range [1, 6000].
* All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.


BellmanFord
```python
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
```

Dijkstra
```python
import collections
import heapq


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
```

Floyd-Warshall
```python
class SolutionFloydWarshall(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        MAX_REACHABLE_TIME = 101 * 100

        distances = [[MAX_REACHABLE_TIME] * N for _ in range(N)]

        for time in times:
            distances[time[0] - 1][time[1] - 1] = time[2]

        for i in range(N):
            distances[i][i] = 0

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    distances[i][j] = min(
                        distances[i][j],
                        distances[i][k] + distances[k][j],
                    )

        max_distance = max(distances[K - 1])

        return -1 if max_distance == MAX_REACHABLE_TIME else max_distance
```
