# [UnionFind]
# https://leetcode.com/problems/redundant-connection/
# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has
# no cycles.
#
# The given input is a graph that started as a tree with N nodes (with
# distinct values 1, 2, ..., N), with one additional edge added. The added
# edge has two different vertices chosen from 1 to N, and was not an edge
# that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
#
# Return an edge that can be removed so that the resulting graph is a tree
# of N nodes. If there are multiple answers, return the answer that occurs
# last in the given 2D-array. The answer edge [u, v] should be in the same
# format, with u < v.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
#
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3


class UnionFindSet(object):
    def __init__(self, n):
        self.parent = range(n)

    def find_root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find_root(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)

        if root_i == root_j:
            return False
        else:
            self.parent[root_i] = root_j
            return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find_set = UnionFindSet(len(edges))

        for i, j in edges:
            if not union_find_set.union(i - 1, j - 1):
                return [i, j]

        return None
