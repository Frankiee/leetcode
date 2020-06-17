# https://leetcode.com/problems/bomb-enemy/
# 361. Bomb Enemy

# History:
# Google
# 1.
# Mar 17, 2020

# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits
# the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.
#
# Example:
#
# Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3
# Explanation: For the given grid,
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# Placing a bomb at (1,1) kills 3 enemies.


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        dp = [[0] * len(grid[0]) for r in range(len(grid))]

        for r in range(len(grid)):
            curr_enermy = 0
            for c in range(len(grid[0])):
                if grid[r][c] == 'E':
                    curr_enermy += 1
                elif grid[r][c] == '0':
                    dp[r][c] += curr_enermy
                else:
                    curr_enermy = 0

        for r in range(len(grid)):
            curr_enermy = 0
            for c in range(len(grid[0]) - 1, -1, -1):
                if grid[r][c] == 'E':
                    curr_enermy += 1
                elif grid[r][c] == '0':
                    dp[r][c] += curr_enermy
                else:
                    curr_enermy = 0

        for c in range(len(grid[0])):
            curr_enermy = 0
            for r in range(len(grid)):
                if grid[r][c] == 'E':
                    curr_enermy += 1
                elif grid[r][c] == '0':
                    dp[r][c] += curr_enermy
                else:
                    curr_enermy = 0

        ret = 0
        for c in range(len(grid[0])):
            curr_enermy = 0
            for r in range(len(grid) - 1, -1, -1):
                if grid[r][c] == 'E':
                    curr_enermy += 1
                elif grid[r][c] == '0':
                    dp[r][c] += curr_enermy
                    ret = max(ret, dp[r][c])
                else:
                    curr_enermy = 0

        return ret
