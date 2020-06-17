# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands

# History:
# Facebook
# 1.
# Mar 7, 2020
# 2.
# Apr 28, 2020

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is
# surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
# may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


class Solution(object):
    def _dfs(self, grid, r, c):
        grid[r][c] = '0'
        for n_r, n_c in [(r + 1, c), [r - 1, c], [r, c + 1], [r, c - 1]]:
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] == '1':
                self._dfs(grid, n_r, n_c)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ret += 1
                    self._dfs(grid, r, c)

        return ret
