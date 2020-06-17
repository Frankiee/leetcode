# [Classic, Encoding-Decoding]
# https://leetcode.com/problems/number-of-distinct-islands/
# 694. Number of Distinct Islands

# History:
# Apple, Cruise
# 1.
# Mar 9, 2020
# 2.
# May 17, 2020

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
# are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and
# only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.


class Solution(object):
    def _dfs(self, grid, r, c):
        ret = ""
        grid[r][c] = 0

        for nxt_r, nxt_c, direction in [(r - 1, c, 'u'), (r + 1, c, 'd'), (r, c - 1, 'l'),
                                        (r, c + 1, 'r')]:
            if 0 <= nxt_r < len(grid) and 0 <= nxt_c < len(grid[0]) and grid[nxt_r][nxt_c] == 1:
                ret += direction
                ret += self._dfs(grid, nxt_r, nxt_c)
                ret += "#"

        return ret

    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        islands_serializsed = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islands_serializsed.add(self._dfs(grid, r, c))

        return len(islands_serializsed)
