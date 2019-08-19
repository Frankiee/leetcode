# [Important]
# https://leetcode.com/problems/max-area-of-island/
# 695. Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of
# 1's (representing land) connected 4-directionally (horizontal or
# vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the
# island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


class Solution(object):
    def calculat_area(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][
            c] == 0:
            return 0

        grid[r][c] = 0
        return (
            1 +
            self.calculat_area(grid, r - 1, c) +
            self.calculat_area(grid, r + 1, c) +
            self.calculat_area(grid, r, c - 1) +
            self.calculat_area(grid, r, c + 1)
        )

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_island = max(max_island, self.calculat_area(grid, r, c))

        return max_island
