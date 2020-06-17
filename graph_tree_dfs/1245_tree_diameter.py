# [Classic, DFS-Parent-Child]
# https://leetcode.com/problems/tree-diameter/
# 1245. Tree Diameter

# History:
# Facebook
# 1.
# Mar 5, 2020
# 2.
# Apr 30, 2020

# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
#
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between
# nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.
#
#
#
# Example 1:
#
#
#
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation:
# A longest path of the tree is the path 1 - 0 - 2.
# Example 2:
#
#
#
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation:
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
#
#
# Constraints:
#
# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# The given edges form an undirected tree.


from collections import defaultdict


class SolutionBFS(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        neighbours = defaultdict(list)

        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        to_do = [0]
        visited = {0}

        node = None
        while to_do:
            nxt_to_do = []

            for e in to_do:
                for nei in neighbours[e]:
                    if nei not in visited:
                        visited.add(nei)
                        nxt_to_do.append(nei)

            if not nxt_to_do:
                node = to_do[0]
                break

            to_do = nxt_to_do

        to_do = [node]
        visited = {node}
        diameter = -1
        while to_do:
            nxt_to_do = []

            for e in to_do:
                for nei in neighbours[e]:
                    if nei not in visited:
                        visited.add(nei)
                        nxt_to_do.append(nei)

            to_do = nxt_to_do

            diameter += 1

        return diameter


from collections import defaultdict


class SolutionParentChild(object):
    def _dfs(self, node, parent, neighbours):
        nbrs = neighbours[node]

        if not nbrs:
            return 0, 0

        longest, second_longest = 0, 0

        for nbr in nbrs:
            if nbr != parent:
                n_longest, n_second_longest = self._dfs(nbr, node, neighbours)
                self.longest_path = max(self.longest_path, n_longest + n_second_longest)

                ranks = [longest, second_longest, n_longest + 1]
                ranks.sort(reverse=True)
                longest, second_longest = ranks[0], ranks[1]

        self.longest_path = max(self.longest_path, longest + second_longest)
        return longest, second_longest

    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0

        self.longest_path = 0

        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        self._dfs(0, -1, neighbours)

        return self.longest_path


from collections import defaultdict


class Solution(object):
    def _dfs(self, node, visited, neighbours):
        visited.add(node)

        nbrs = [n for n in neighbours[node] if n not in visited]

        if not nbrs:
            return 0, 0

        longest, second_longest = 0, 0

        for n in nbrs:
            if n in visited:
                continue
            n_longest, n_second_longest = self._dfs(n, visited, neighbours)
            self.longest_path = max(self.longest_path, n_longest + n_second_longest)

            ranks = [longest, second_longest, n_longest + 1]
            ranks.sort(reverse=True)
            longest, second_longest = ranks[0], ranks[1]

        self.longest_path = max(self.longest_path, longest + second_longest)
        return longest, second_longest

    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0

        self.longest_path = 0

        visited = set()

        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        self._dfs(0, visited, neighbours)

        return self.longest_path
