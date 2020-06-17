# [Archived]
# https://leetcode.com/problems/count-servers-that-communicate/
# 1267. Count Servers that Communicate

# History:
# Google
# 1.
# Mar 12, 2020

# You are given a map of a server center, represented as a m * n integer matrix grid,
# where 1 means that on that cell there is a server and 0 means that it is no server. Two servers
# are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.
#
#
#
# Example 1:
#
#
#
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# Example 2:
#
#
#
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.
# Example 3:
#
#
#
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers
# in the third column can communicate with each other. The server at right bottom corner can't
# communicate with any other server.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0

        for r in range(len(grid)):
            count = grid[r].count(1)

            if count > 1:
                for c in range(len(grid[r])):
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        ret += 1

        for c in range(len(grid[0])):
            flipped = 0
            non_flipped = 0
            for r in range(len(grid)):
                if grid[r][c] == 2:
                    flipped += 1
                elif grid[r][c] == 1:
                    non_flipped += 1

            if flipped + non_flipped > 1:
                ret += non_flipped

        return ret
