# [Classic]
# https://leetcode.com/problems/minimum-knight-moves/
# 1197. Minimum Knight Moves

# History:
# Facebook
# 1.
# May 31, 2020

# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at
# square [0, 0].
#
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a
# cardinal direction, then one square in an orthogonal direction.
#
#
#
# Return the minimum number of steps needed to move the knight to the square [x, y].  It is
# guaranteed the answer exists.
#
#
#
# Example 1:
#
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:
#
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#
# Constraints:
#
# |x| + |y| <= 300


class Solution(object):
    def _dfs(self, x, y, mem):
        if (x, y) in mem:
            return mem[(x, y)]

        if x + y == 0:
            ret = 0
        elif x + y == 2:
            ret = 2
        else:
            ret = min(
                self._dfs(abs(x - 2), abs(y - 1), mem),
                self._dfs(abs(x - 1), abs(y - 2), mem),
            ) + 1

        mem[(x, y)] = ret

        return ret

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = abs(x), abs(y)
        mem = {}

        return self._dfs(x, y, mem)
