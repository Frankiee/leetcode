# [Cycle-Detection, Classic]
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
# Detect Cycle in a Directed Graph

# History:
# 1.
# Nov 2, 2019
# Daily Interview Pro

# Given a directed graph, check whether the graph contains a cycle or not.
# Your function should return true if the given graph contains at least one cycle, else return false
# For example, the following graph contains three cycles 0->2->0, 0->1->2->0 and 3->3
# so your function must return true.


from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle(self, vertex, visited, visit_stack):
        visited[vertex] = True
        visit_stack[vertex] = True

        for n in self.graph[vertex]:
            if visited[n] and visit_stack[n]:
                return True
            if not visited[n] and self.has_cycle(n, visited, visit_stack):
                return True

        visit_stack[vertex] = False

        return False

    # Returns true if graph is cyclic else false
    def is_cyclic(self):
        visited = [False] * self.vertices
        visit_stack = [False] *  self.vertices

        for v in range(self.vertices):
            if v not in visited:
                if self.has_cycle(v, visited, visit_stack):
                    return True

        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
if g.is_cyclic() == 1:
    print "Graph has a cycle"
else:
    print "Graph has no cycle"
