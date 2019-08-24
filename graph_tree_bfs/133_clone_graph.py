# https://leetcode.com/problems/clone-graph/
# 133. Clone Graph

# Given a reference of a node in a connected undirected graph, return a deep
# copy (clone) of the graph. Each node in the graph contains a val (int) and
# a list (List[Node]) of its neighbors.
#
#
#
# Example:
#
# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3",
# "neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},
# {"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
#
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
#
#
# Note:
#
# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and
# no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node
# q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned
# graph.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = set()
        clone_map = {}

        to_visit = [node]
        res = None

        while to_visit:
            next_visit = None
            while to_visit:
                next_try = to_visit.pop(0)
                if next_try in visited:
                    continue
                else:
                    next_visit = next_try
                    break

            if not next_visit:
                return res

            if next_visit in clone_map:
                clone = clone_map[next_visit]
            else:
                clone = Node(next_visit.val, None)
                clone_map[next_visit] = clone
            clone_neighbors = []
            for n in next_visit.neighbors:
                if n in clone_map:
                    clone_n = clone_map[n]
                else:
                    clone_n = Node(n.val, None)
                    clone_map[n] = clone_n
                clone_neighbors.append(clone_n)
            clone.neighbors = clone_neighbors

            if not res:
                res = clone
            visited.add(next_visit)
            for n in next_visit.neighbors:
                if n not in visited:
                    to_visit.append(n)
        return res
