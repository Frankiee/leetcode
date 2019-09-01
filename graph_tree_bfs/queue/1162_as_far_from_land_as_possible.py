# [Hard, BFS, Queue]
# https://leetcode.com/problems/as-far-from-land-as-possible/
# 1162. As Far from Land as Possible

# Given an N x N grid containing only values 0 and 1, where 0 represents
# water and 1 represents land, find a water cell such that its distance to
# the nearest land cell is maximized and return the distance.
#
# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
# If no land or water exists in the grid, return -1.
#
#
# Example 1:
#
#
# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation:
# The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:
#
#
#
# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation:
# The cell (2, 2) is as far as possible from all the land with distance 4.
#
#
# Note:
#
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        to_visit = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = '#'
                    to_visit.append((r, c))

        max_distance = -1

        while to_visit:
            r, c = to_visit.pop(0)
            current_distance = grid[r][c]

            if current_distance == '#':
                next_distance = 1
            else:
                next_distance = current_distance + 1

            # up
            if r >= 1 and grid[r - 1][c] == 0:
                grid[r - 1][c] = next_distance
                to_visit.append((r - 1, c))
                max_distance = max(max_distance, next_distance)
            # down
            if r + 1 < len(grid) and grid[r + 1][c] == 0:
                grid[r + 1][c] = next_distance
                to_visit.append((r + 1, c))
                max_distance = max(max_distance, next_distance)
            # left
            if c >= 1 and grid[r][c - 1] == 0:
                grid[r][c - 1] = next_distance
                to_visit.append((r, c - 1))
                max_distance = max(max_distance, next_distance)
            # right
            if c + 1 < len(grid[0]) and grid[r][c + 1] == 0:
                grid[r][c + 1] = next_distance
                to_visit.append((r, c + 1))
                max_distance = max(max_distance, next_distance)

        return max_distance
