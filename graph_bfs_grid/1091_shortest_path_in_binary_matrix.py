# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# 1091. Shortest Path in Binary Matrix

# History:
# 1.
# Mar 7, 2020
# 2.
# Apr 28, 2020

# In an N by N square grid, each cell is either empty (0) or blocked (1).
#
# A clear path from top-left to bottom-right has length k if and only if it is composed of cells
# C_1, C_2, ..., C_k such that:
#
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share
# an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a
# path does not exist, return -1.
#
#
#
# Example 1:
#
# Input: [[0,1],[1,0]]
#
#
# Output: 2
#
# Example 2:
#
# Input: [[0,0,0],[1,1,0],[1,1,0]]
#
#
# Output: 4
#
#
#
# Note:
#
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        to_do = [(0, 0)]
        grid[0][0] = 2

        s = 1
        while to_do:
            nxt_to_do = []

            for r, c in to_do:
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return s

                for n_r, n_c in [
                        (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c + 1),
                        (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)]:
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] == 0:
                        nxt_to_do.append((n_r, n_c))
                        grid[n_r][n_c] = 2

            s += 1
            to_do = nxt_to_do

        return -1
