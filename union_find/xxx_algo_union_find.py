# [Union-Find, Algorithm]
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
        self.parents = range(n)
        self.ranks = [0] * n

    def find_root(self, i):
        # Path compression
        if i != self.parents[i]:
            # If i is not root
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]

    def _union_two(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if self.ranks[i_root] < self.ranks[j_root]:
            self.parents[i_root] = j_root
        elif self.ranks[j_root] < self.ranks[i_root]:
            self.parents[j_root] = i_root
        else:   # Equal
            self.parents[i_root] = j_root
            self.ranks[j_root] += 1

    def union(self, lst):
        fst = lst[0]

        for l in lst[1:]:
            self._union_two(fst, l)


class UnionFindDict(object):
    def __init__(self):
        self.parents = {}
        self.rank = defaultdict(int)

    def find_root(self, i):
        if i not in self.parents:
            self.parents[i] = i
        else:
            if self.parents[i] != i:
                self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if i_root == j_root:
            return

        if self.rank[i_root] > self.rank[j_root]:
            self.parents[j_root] = i_root
        elif self.rank[i_root] < self.rank[j_root]:
            self.parents[i_root] = j_root
        else:
            self.parents[i_root] = j_root
            self.rank[j_root] += 1
