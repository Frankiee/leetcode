# [Classic, BFS, Queue]
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# 847. Shortest Path Visiting All Nodes

# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is
# given as graph.
#
# graph.length = N, and j != i is in the list graph[i] exactly once, if and
# only if nodes i and j are connected.
#
# Return the length of the shortest path that visits every node. You may
# start and stop at any node, you may revisit nodes multiple times, and you
# may reuse edges.
#
#
#
# Example 1:
#
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:
#
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#
#
# Note:
#
# 1 <= graph.length <= 12
# 0 <= graph[i].length < graph.length


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        visited_memo = set()
        final_state = (1 << len(graph)) - 1
        nodes_to_visit = []
        for label in range(len(graph)):
            nodes_to_visit.append((
                label,
                0,
                1 << label,
            ))

        while nodes_to_visit:
            node_label, steps, visited = nodes_to_visit.pop(0)
            if visited == final_state:
                return steps

            neighbours = graph[node_label]
            for n in neighbours:
                if (visited | 1 << n, n) not in visited_memo:
                    nodes_to_visit.append((
                        n,
                        steps + 1,
                        visited | 1 << n,
                    ))
                    visited_memo.add((visited | 1 << n, n))
