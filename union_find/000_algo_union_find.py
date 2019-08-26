# [Union-Find]
# https://www.youtube.com/watch?v=VJnUwsE4fWA&t=397s


# Basic UnionFind
class UnionFindSet(object):
    def __init__(self, n):
        self.parent = range(n)

    def find_root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find_root(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parent[i_root] = j_root


# UnionFind with More Balanced Tree
class UnionFindSetWithRanks(object):
    def __init__(self, n):
        self.roots = range(n)
        self.ranks = [0] * n

    def find_root(self, i):
        # Path compression
        if i != self.roots[i]:
            # If i is not root
            self.roots[i] = self.find_root(self.roots[i])

        return self.roots[i]

    def _union_two(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if self.ranks[i_root] > self.ranks[j_root]:
            self.roots[i_root] = j_root
        elif self.ranks[j_root] > self.ranks[i_root]:
            self.roots[j_root] = i_root
        else:   # Equal
            self.roots[i_root] = j_root
            self.ranks[i_root] += 1

    def union(self, lst):
        fst = lst[0]

        for l in lst[1:]:
            self._union_two(fst, l)
