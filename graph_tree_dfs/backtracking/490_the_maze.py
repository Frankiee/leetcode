# [Backtracking, Classic]
# https://leetcode.com/problems/the-maze/
# 490. The Maze

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# May 10, 2020

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by
# rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball
# stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, determine whether the ball could
# stop at the destination.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You
# may assume that the borders of the maze are all walls. The start and destination coordinates
# are represented by row and column indexes.
#
#
#
# Example 1:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: true
#
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
#
# Example 2:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: false
#
# Explanation: There is no way for the ball to stop at the destination.
#
#
#
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same
# position initially.
# The given maze does not contain border (like the red rectangle in the example pictures),
# but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't
# exceed 100.


class Solution(object):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def _move(self, maze, start, direction):
        curr_x, curr_y = start
        delta_x, delta_y = direction

        nxt_x, nxt_y = curr_x + delta_x, curr_y + delta_y
        while 0 <= nxt_x < len(maze) and 0 <= nxt_y < len(maze[0]) and maze[nxt_x][nxt_y] == 0:
            curr_x, curr_y = nxt_x, nxt_y

            nxt_x, nxt_y = curr_x + delta_x, curr_y + delta_y

        return curr_x, curr_y

    def _dfs(self, maze, curr, destination, visited):
        if curr == destination:
            return True

        for direction in [self.UP, self.DOWN, self.LEFT, self.RIGHT]:
            nxt = self._move(maze, curr, direction)
            if nxt not in visited:
                visited.add(nxt)

                if self._dfs(maze, nxt, destination, visited):
                    return True

        return False

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        destination = tuple(destination)
        visited = {tuple(start)}
        return self._dfs(maze, start, destination, visited)
