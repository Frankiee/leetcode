# [Cycle-Detection, Classic]
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
# Detect cycle in an undirected graph

# History:
# 1.
# Nov 2, 2019
# Daily Interview Pro


from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    def has_cycle(self, vertex, parent, visited):
        visited[vertex] = True
        for n in self.graph[vertex]:
            if n in visited and n != parent:
                return True
            if n not in visited and self.has_cycle(n, vertex, visited):
                return True

        return False

    # Returns true if the graph contains a cycle, else false.
    def is_cyclic(self):
        visited = {}

        for v in range(self.vertices):
            if v not in visited:
                if self.has_cycle(v, None, visited):
                    return True

        return False


# Create a graph given in the above diagram
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.is_cyclic():
    print "Graph contains cycle"
else:
    print "Graph does not contain cycle "
g1 = Graph(3)
g1.add_edge(0, 1)
g1.add_edge(1, 2)

if g1.is_cyclic():
    print "Graph contains cycle"
else:
    print "Graph does not contain cycle "
