# https://leetcode.com/problems/walls-and-gates/
# 286. Walls and Gates

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# Apr 28, 2020

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as
# you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a
# gate, it should be filled with INF.
#
# Example:
#
# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4


class Solution(object):
    INF = 2147483647

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        to_do = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    to_do.append((r, c))

        while to_do:
            nxt_to_do = []
            for (r, c) in to_do:
                val = rooms[r][c]

                for nxt_r, nxt_c in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                    if (0 <= nxt_r < len(rooms) and 0 <= nxt_c < len(rooms[0]) and
                            rooms[nxt_r][nxt_c] == self.INF):
                        rooms[nxt_r][nxt_c] = val + 1
                        nxt_to_do.append((nxt_r, nxt_c))

            to_do = nxt_to_do
