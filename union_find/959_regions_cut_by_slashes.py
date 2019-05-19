# https://leetcode.com/problems/regions-cut-by-slashes/
# 959. Regions Cut By Slashes

# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a
# /, \, or blank space.  These characters divide the square into contiguous
# regions.
#
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
#
# Return the number of regions.
#
#
#
# Example 1:
#
# Input:
# [
#   " /",
#   "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:
#
# Example 2:
#
# Input:
# [
#   " /",
#   "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:
#
# Example 3:
#
# Input:
# [
#   "\\/",
#   "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers
# to \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:
#
# Example 4:
#
# Input:
# [
#   "/\\",
#   "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers
# to /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:
#
# Example 5:
#
# Input:
# [
#   "//",
#   "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:
#
#
#
# Note:
#
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.


class UnionFindSet(object):
    def __init__(self, n):
        self.roots = range(n)

    def find_root(self, i):
        if i != self.roots[i]:
            self.roots[i] = self.find_root(self.roots[i])

        return self.roots[i]

    def _union_two(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.roots[i_root] = j_root

    def union(self, lst):
        fst = lst[0]

        for l in lst[1:]:
            self._union_two(fst, l)


class Solution(object):
    def _get_square_idx(self, r, c, square_region):
        # For square_region
        # 0: up, 1: left, 2: right 3: bottom

        return r * 4 * self.N + c * 4 + square_region

    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid:
            return 0

        self.N = len(grid)

        total_regions = 4 * self.N * self.N
        union_find_set = UnionFindSet(total_regions)

        for r in range(self.N):
            for c in range(self.N):
                square = grid[r][c]
                # current
                if square == ' ':
                    union_find_set.union([
                        self._get_square_idx(r, c, 0),
                        self._get_square_idx(r, c, 1),
                        self._get_square_idx(r, c, 2),
                        self._get_square_idx(r, c, 3),
                    ])
                elif square == '/':
                    union_find_set.union([
                        self._get_square_idx(r, c, 0),
                        self._get_square_idx(r, c, 1),
                    ])
                    union_find_set.union([
                        self._get_square_idx(r, c, 2),
                        self._get_square_idx(r, c, 3),
                    ])
                elif square == '\\':
                    union_find_set.union([
                        self._get_square_idx(r, c, 0),
                        self._get_square_idx(r, c, 2),
                    ])
                    union_find_set.union([
                        self._get_square_idx(r, c, 1),
                        self._get_square_idx(r, c, 3),
                    ])

                # Up
                if r > 0:
                    union_find_set.union([
                        self._get_square_idx(r, c, 0),
                        self._get_square_idx(r - 1, c, 3),
                    ])
                # Down
                if c > 0:
                    union_find_set.union([
                        self._get_square_idx(r, c, 1),
                        self._get_square_idx(r, c - 1, 2),
                    ])

        regions = set()
        for region_idx in range(total_regions):
            regions.add(
                union_find_set.find_root(region_idx)
            )

        return len(regions)
