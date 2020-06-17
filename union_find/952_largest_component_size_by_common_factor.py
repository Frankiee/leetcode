# [Union-Find, Prime-Factor]
# https://leetcode.com/problems/largest-component-size-by-common-factor/
# 952. Largest Component Size by Common Factor

# History:
# 1.
# Sep 1, 2019
# 2.
# Nov 13, 2019

# Given a non-empty array of unique positive integers A, consider the
# following graph:
#
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share
# a common factor greater than 1.
# Return the size of the largest connected component in the graph.
#
# Example 1:
#
# Input: [4,6,15,35]
# Output: 4
#
# Example 2:
#
# Input: [20,50,9,63]
# Output: 2
#
# Example 3:
#
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
#
# Note:
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000


from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.parent = range(n)

    def find_root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find_root(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if i_root == j_root:
            return True
        else:
            self.parent[i_root] = j_root
            return False


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = max(A)

        uf = UnionFind(n + 1)

        for a in A:
            for k in range(2, int(math.sqrt(a)) + 1):
                if a % k == 0:
                    uf.union(a, k)
                    uf.union(a, a / k)

        c = defaultdict(int)
        max_count = 0
        for a in A:
            root = uf.find_root(a)

            c[root] += 1
            max_count = max(max_count, c[root])

        return max_count
