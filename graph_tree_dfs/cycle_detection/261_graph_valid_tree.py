# [Cycle-Detection, Classic]
# https://leetcode.com/problems/graph-valid-tree/
# 261. Graph Valid Tree

# History:
# Facebook
# 1.
# Mar 19, 2020

# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of
# nodes), write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are
# undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


from collections import defaultdict


class Solution(object):
    def _has_cycle(self, node, parent, graph, visited):
        visited[node] = True

        for nei in graph[node]:
            if visited[nei] and nei != parent:
                return True
            if not visited[nei] and self._has_cycle(nei, node, graph, visited):
                return True

        return False

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        # Visit one node, make sure afterwards all other nodes are visited
        if self._has_cycle(0, None, graph, visited):
            return False

        for node in range(n):
            if not visited[node]:
                return False

        return True
