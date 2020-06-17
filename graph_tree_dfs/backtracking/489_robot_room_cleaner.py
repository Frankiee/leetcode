# [Backtracking, Classic]
# https://leetcode.com/problems/robot-room-cleaner/
# 489. Robot Room Cleaner

# History:
# Facebook
# 1.
# Mar 1, 2020
# 2.
# May 12, 2020

# Given a robot cleaner in a room modeled as a grid.
#
# Each cell in the grid can be empty or blocked.
#
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it
# made is 90 degrees.
#
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays
# on the current cell.
#
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }
# Example:
#
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
#
# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns right.
# Notes:
#
# The input is only given to initialize the room and the robot's position internally. You must
# solve this problem "blindfolded". In other words, you must control the robot using only the
# mentioned 4 APIs, without knowing the room layout and the initial robot's position.
# The robot's initial position will always be in an accessible cell.
# The initial direction of the robot will be facing up.
# All accessible cells are connected, which means the all cells marked as 1 will be accessible by
# the robot.
# Assume all four edges of the grid are all surrounded by wall.


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution1(object):
    def _dfs(self, robot):
        self.visited.add((self.r, self.c))
        robot.clean()

        # move up
        if (self.r - 1, self.c) not in self.visited:
            moved = robot.move()
            if moved:
                self.r -= 1
                self._dfs(robot)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
                self.r += 1

        robot.turnRight()
        if (self.r, self.c + 1) not in self.visited:
            moved = robot.move()
            if moved:
                self.c += 1
                robot.turnLeft()
                self._dfs(robot)
                robot.turnLeft()
                robot.move()
                robot.turnRight()
                robot.turnRight()
                self.c -= 1

        robot.turnRight()
        if (self.r + 1, self.c) not in self.visited:
            moved = robot.move()
            if moved:
                self.r += 1
                robot.turnRight()
                robot.turnRight()
                self._dfs(robot)
                robot.move()
                robot.turnRight()
                robot.turnRight()
                self.r -= 1

        robot.turnRight()
        if (self.r, self.c - 1) not in self.visited:
            moved = robot.move()
            if moved:
                self.c -= 1
                robot.turnRight()
                self._dfs(robot)
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
                self.c += 1

        robot.turnRight()

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = set()

        self.r, self.c = 0, 0

        self._dfs(robot)


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution2(object):
    FACING_UP = 1
    FACING_RIGHT = 2
    FACING_DOWN = 3
    FACING_LEFT = 4

    TURN_RIGHT_FACING_NEXT_STATE = {
        FACING_UP: FACING_RIGHT,
        FACING_RIGHT: FACING_DOWN,
        FACING_DOWN: FACING_LEFT,
        FACING_LEFT: FACING_UP,
    }

    def _turn(self, dest_facing):
        while self.facing != dest_facing:
            self.robot.turnRight()
            self.facing = self.TURN_RIGHT_FACING_NEXT_STATE[self.facing]

    def _dfs(self, robot):
        robot.clean()
        self.visited.add((self.r, self.c))

        # up
        if (self.r - 1, self.c) not in self.visited:
            self._turn(self.FACING_UP)
            moved = robot.move()
            if moved:
                self.r -= 1
                self._dfs(robot)

                # return
                self._turn(self.FACING_DOWN)
                robot.move()
                self.r += 1

        # left
        if (self.r, self.c - 1) not in self.visited:
            self._turn(self.FACING_LEFT)
            moved = robot.move()
            if moved:
                self.c -= 1
                self._dfs(robot)

                # return
                self._turn(self.FACING_RIGHT)
                robot.move()
                self.c += 1

        # down
        if (self.r + 1, self.c) not in self.visited:
            self._turn(self.FACING_DOWN)
            moved = robot.move()
            if moved:
                self.r += 1
                self._dfs(robot)

                # return
                self._turn(self.FACING_UP)
                robot.move()
                self.r -= 1

        # right
        if (self.r, self.c + 1) not in self.visited:
            self._turn(self.FACING_RIGHT)
            moved = robot.move()
            if moved:
                self.c += 1
                self._dfs(robot)

                # return
                self._turn(self.FACING_LEFT)
                robot.move()
                self.c -= 1

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.facing = self.FACING_UP
        self.r = 0
        self.c = 0

        self.visited = set()

        self._dfs(robot)
