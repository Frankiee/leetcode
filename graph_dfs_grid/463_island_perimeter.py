# https://leetcode.com/problems/island-perimeter/
# 463. Island Perimeter

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 13, 2020
# 3.
# May 2, 2020

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0
# represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
# surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the
# island). One cell is a square with side length 1. The grid is rectangular, width and height
# don't exceed 100. Determine the perimeter of the island.
#
#
#
# Example:
#
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def _dfs(self, grid, r, c):
        grid[r][c] = 2

        ret = 0
        for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]):
                if grid[n_r][n_c] == 0:
                    ret += 1
                if grid[n_r][n_c] == 1:
                    ret += self._dfs(grid, n_r, n_c)
            else:
                ret += 1

        return ret

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return self._dfs(grid, r, c)
