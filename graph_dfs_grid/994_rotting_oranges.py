# https://leetcode.com/problems/rotting-oranges/
# 994. Rotting Oranges

# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a
# rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
#
#
#
# Example 1:
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is
# never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0,
# the answer is just 0.
#
#
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1

        changed = False
        minutes = 0

        while fresh > 0:
            skip = set()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 2 and (r, c) not in skip:
                        # Up
                        if r > 0 and grid[r - 1][c] == 1:
                            grid[r - 1][c] = 2
                            changed = True
                            fresh -= 1
                            skip.add((r - 1, c))
                        # Down
                        if r + 1 <= len(grid) - 1 and grid[r + 1][c] == 1:
                            grid[r + 1][c] = 2
                            changed = True
                            fresh -= 1
                            skip.add((r + 1, c))
                        # Left
                        if c > 0 and grid[r][c - 1] == 1:
                            grid[r][c - 1] = 2
                            changed = True
                            fresh -= 1
                            skip.add((r, c - 1))
                        # Right
                        if c + 1 <= len(grid[0]) - 1 and grid[r][c + 1] == 1:
                            grid[r][c + 1] = 2
                            changed = True
                            fresh -= 1
                            skip.add((r, c + 1))
            if not changed:
                return -1

            changed = False
            minutes += 1
            skip = set()

        return minutes
