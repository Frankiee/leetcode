# [Union-Find]
# https://leetcode.com/problems/regions-cut-by-slashes/
# 959. Regions Cut By Slashes

# https://www.youtube.com/watch?v=n3s9Q7GtfB4&t=133s

# History:
# 1.
# May 20, 2019
# 2.
# Nov 17, 2019

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
        self.parents = range(n)

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parents[i_root] = j_root

    def find_root(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0:
            return 0

        sides = len(grid)

        union_find = UnionFindSet(4 * sides * sides)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                base = 4 * (sides * r + c)

                if c > 0:
                    union_find.union(base, base - 2)
                if r > 0:
                    union_find.union(base + 1, 4 * (sides * (r - 1) + c) + 3)
                if grid[r][c] == '\\' or grid[r][c] == ' ':
                    union_find.union(base, base + 3)
                    union_find.union(base + 1, base + 2)
                if grid[r][c] == '/' or grid[r][c] == ' ':
                    union_find.union(base, base + 1)
                    union_find.union(base + 2, base + 3)

        ret_set = set()
        for i in range(4 * sides * sides):
            ret_set.add(union_find.find_root(i))

        return len(ret_set)
