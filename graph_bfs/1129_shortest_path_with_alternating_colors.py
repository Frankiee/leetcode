# [Important]
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# 1129. Shortest Path with Alternating Colors

# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this
# graph, each edge is either red or blue, and there could be self-edges or
# parallel edges.
#
# Each [i, j] in red_edges denotes a red directed edge from node i to node
# j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from
# node i to node j.
#
# Return an array answer of length n, where each answer[X] is the length of
# the shortest path from node 0 to node X such that the edge colors
# alternate along the path (or -1 if such a path doesn't exist).
#
#
# Example 1:
#
# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
#
# Example 2:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
#
# Example 3:
#
# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
#
# Example 4:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
#
# Example 5:
#
# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
#
#
# Constraints:
#
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n

from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        ret = [float('inf')] * n

        red_paths = defaultdict(list)
        blue_paths = defaultdict(list)
        for start, end in red_edges:
            red_paths[start].append(end)
        for start, end in blue_edges:
            blue_paths[start].append(end)

        current_step = 0
        # (label, color) where 0: red, 1: blue
        current_nodes = [(0, 0), (0, 1)]
        visited = {(0, 0), (0, 1)}

        while current_nodes:
            next_current_nodes = []
            for node in current_nodes:
                current_label, current_color = node
                ret[current_label] = min(ret[current_label], current_step)

                next_color = 1 if current_color == 0 else 0
                next_paths = blue_paths if current_color == 0 else red_paths
                next_nodes = [
                    (next_label, next_color)
                    for next_label in next_paths[current_label]
                    if (next_label, next_color) not in visited
                ]
                next_current_nodes.extend(next_nodes)
                visited |= set(next_nodes)

            current_nodes = next_current_nodes
            current_step += 1

        ret = [-1 if r == float('inf') else r for r in ret]
        return ret
