# [Union-Find]
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# 323. Number of Connected Components in an Undirected Graph

# History:
# Facebook
# 1.
# Mar 7, 2020
# 2.
# May 3, 2020

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of
# nodes), write a function to find the number of connected components in an undirected graph.
#
# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.


class UnionFind1(object):
    def __init__(self, n):
        self.parents = range(n)

    def find_root(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parents[i_root] = j_root


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)

        for i, j in edges:
            union_find.union(i, j)

        roots = set()

        for i in range(n):
            roots.add(union_find.find_root(i))

        return len(roots)


class UnionFind2(object):
    def __init__(self):
        self.parent = {}

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parent[i_root] = j_root

    def find_root(self, i):
        if i not in self.parent:
            self.parent[i] = i
        else:
            if self.parent[i] != i:
                self.parent[i] = self.find_root(self.parent[i])

        return self.parent[i]


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind()

        for i, j in edges:
            union_find.union(i, j)

        roots = set()
        for i in range(n):
            roots.add(union_find.find_root(i))

        return len(roots)


from collections import defaultdict


class SolutionDFS(object):
    def _dfs(self, i, visited, neis):
        visited.add(i)

        for nei in neis[i]:
            if nei not in visited:
                self._dfs(nei, visited, neis)

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = set()
        neis = defaultdict(list)

        for i, j in edges:
            neis[i].append(j)
            neis[j].append(i)

        ret = 0
        for i in range(n):
            if i not in visited:
                ret += 1
                self._dfs(i, visited, neis)

        return ret
