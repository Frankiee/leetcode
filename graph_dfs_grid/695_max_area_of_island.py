# https://leetcode.com/problems/max-area-of-island/
# 695. Max Area of Island

# History:
# Facebook
# 1.
# Apr 17, 2019
# 2.
# Apr 28, 2020

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
    def count_area(self, grid, r, c):
        ret = 1
        grid[r][c] = 0

        for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] == 1:
                ret += self.count_area(grid, n_r, n_c)

        return ret

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ret = max(ret, self.count_area(grid, r, c))

        return ret
