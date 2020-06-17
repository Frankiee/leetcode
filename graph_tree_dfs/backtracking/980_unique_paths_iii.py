# [Backtracking, Classic]
# https://leetcode.com/problems/unique-paths-iii/
# 980. Unique Paths III

# History:
# TikTok
# 1.
# Apr 26, 2020

# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.
#
#
#
# Example 1:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:
#
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
# Note:
#
# 1 <= grid.length * grid[0].length <= 20


class Solution(object):
    def _dfs(self, grid, r, c, zeros_left):
        if grid[r][c] == 2:
            if zeros_left == 0:
                self.ret += 1
            return

        old = grid[r][c]
        grid[r][c] = -1
        if old == 0:
            zeros_left -= 1
        for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] in {0, 2}:
                self._dfs(grid, n_r, n_c, zeros_left)

        grid[r][c] = old
        if old == 0:
            zeros_left += 1

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        zeros_left = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    zeros_left += 1

        self.ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self._dfs(grid, r, c, zeros_left)

        return self.ret
