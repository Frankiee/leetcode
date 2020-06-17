# [Union-Find, Classic]
# https://leetcode.com/problems/number-of-islands-ii/
# 305. Number of Islands II

# History:
# Cruise Interview
# 1.
# Mar 26, 2020
# 2.
# Apr 29, 2020

# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand
# operation which turns the water at position (row, col) into a land. Given a list of positions
# to operate, count the number of islands after each addLand operation. An island is surrounded
# by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water.
#
# Example:
#
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# Explanation:
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents
# land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# Follow up:
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions?


from collections import defaultdict


class UnionFindSet(object):
    def __init__(self):
        self.parents = {}
        self.ranks = defaultdict(int)

    def find_root(self, i):
        if i not in self.parents:
            self.parents[i] = i
        elif i != self.parents[i]:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if i_root == j_root:
            return

        if self.ranks[i_root] > self.ranks[j_root]:
            self.parents[j_root] = i_root
        elif self.ranks[i_root] < self.ranks[j_root]:
            self.parents[i_root] = j_root
        else:
            self.parents[i_root] = j_root
            self.ranks[j_root] += 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0] * n for _ in range(m)]
        union_find_set = UnionFindSet()

        ret = []
        curr_islands = 0
        for r, c in positions:
            if grid[r][c] != 1:
                island_roots = set()
                grid[r][c] = 1

                for n_r, n_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == 1:
                        root = union_find_set.find_root((n_r, n_c))

                        if root not in island_roots:
                            island_roots.add(root)
                            union_find_set.union((r, c), (n_r, n_c))

                curr_islands += 1 - len(island_roots)
            ret.append(curr_islands)

        return ret


class UnionFindByIndex(object):
    def __init__(self, n):
        self.parents = range(n)

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parents[i_root] = j_root

    def find_root(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]


class SolutionUnionFindByIndex(object):
    def _cell_to_union_find_idx(self, r, c):
        return self.n * r + c

    def _apply_operation(self, operation):
        r, c = operation

        if self.board[r][c] == 1:
            return self.curr_islands_count
        self.board[r][c] = 1

        node_idx = self._cell_to_union_find_idx(r, c)

        pre_unique_islands = set()
        for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= n_r < self.m and 0 <= n_c < self.n and self.board[n_r][n_c] == 1:
                nei_idx = self._cell_to_union_find_idx(n_r, n_c)
                nei_root = self.union_find.find_root(nei_idx)

                if nei_root not in pre_unique_islands:
                    pre_unique_islands.add(nei_root)

                    self.union_find.union(node_idx, nei_idx)

        self.curr_islands_count += 1 - len(pre_unique_islands)

        return self.curr_islands_count

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.m, self.n = m, n
        num_cells = m * n
        self.board = [[0] * n for _ in range(m)]

        self.union_find = UnionFindByIndex(num_cells)

        self.curr_islands_count = 0

        return [self._apply_operation(operation) for operation in positions]
