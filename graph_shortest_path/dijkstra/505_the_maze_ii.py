# [Classic, Dijkstra, Shortest-Path]
# https://leetcode.com/problems/the-maze-ii/
# 505. The Maze II

# History:
# Facebook
# 1.
# Mar 3, 2020

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by
# rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball
# stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, find the shortest distance for
# the ball to stop at the destination. The distance is defined by the number of empty spaces
# traveled by the ball from the start position (excluded) to the destination (included). If the
# ball cannot stop at the destination, return -1.
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
# Output: 12
#
# Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
#              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
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
# Output: -1
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

from heapq import heappush, heappop


class Solution(object):
    DIRECTION_UP = 1
    DIRECTION_DOWN = 2
    DIRECTION_LEFT = 3
    DIRECTION_RIGHT = 4

    def _roll(self, maze, r, c, direction):
        distance = 0
        if direction == self.DIRECTION_UP:
            while r > 0 and maze[r - 1][c] != 1:
                r -= 1
                distance += 1
        elif direction == self.DIRECTION_DOWN:
            while r < len(maze) - 1 and maze[r + 1][c] != 1:
                r += 1
                distance += 1
        elif direction == self.DIRECTION_LEFT:
            while c > 0 and maze[r][c - 1] != 1:
                c -= 1
                distance += 1
        else:
            while c < len(maze[0]) - 1 and maze[r][c + 1] != 1:
                c += 1
                distance += 1

        return r, c, distance

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        start, destination = tuple(start), tuple(destination)

        visited = {
            start: 0,
        }

        to_do = [(0, start)]

        while to_do:
            curr_distance, pos = heappop(to_do)

            if pos == destination:
                return curr_distance

            for direction in [self.DIRECTION_UP, self.DIRECTION_DOWN, self.DIRECTION_LEFT,
                              self.DIRECTION_RIGHT]:
                nxt_r, nxt_c, distance = self._roll(maze, pos[0], pos[1], direction)

                new_distance = curr_distance + distance
                if (nxt_r, nxt_c) not in visited or new_distance < visited[(nxt_r, nxt_c)]:
                    visited[(nxt_r, nxt_c)] = new_distance
                    heappush(to_do, (new_distance, (nxt_r, nxt_c)))

        return -1
