# [Facebook]
# http://www.dailyinterviewpro.com/view.php?pid=123&email=tonylee80%40gmail.com&token=c05f177527b857a4cd97a9f9ef73d144   # noqa
# Reverse a Directed Graph

# History:
# 1.
# Nov 2, 2019
# Daily Interview Pro - Facebook

# Given a directed graph, reverse the directed graph so all directed edges are reversed.
#
# Example:
# Input:
# A -> B, B -> C, A ->C
#
# Output:
# B->A, C -> B, C -> A


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value


def reverse_graph(graph):
    ret_graph = {}

    for _, node in graph.iteritems():
        adjacents = node.adjacent
        if node.value not in ret_graph:
            ret_graph[node.value] = Node(node.value)

        for a in adjacents:
            if a.value not in ret_graph:
                ret_graph[a.value] = Node(a.value)
            ret_graph[a.value].adjacent.append(node)

    return ret_graph


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
    print(val.value, val.adjacent)
# []
# ['a', 'b']
# ['a']
