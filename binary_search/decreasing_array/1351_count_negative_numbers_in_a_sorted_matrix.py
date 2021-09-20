# `Classic` `Decreasing-Array`
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# 1351. Count Negative Numbers in a Sorted Matrix

# History:
# 1.
# Sep 18, 2021

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number
# of negative numbers in grid.
#
#
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
#
# Input: grid = [[-1]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
#
#
# Follow up: Could you find an O(n + m) solution?

class Solution(object):
    def _binary_search(self, arr, l, r):
        while l < r:
            m = (r - l) / 2 + l

            if arr[m] < 0:
                r = m
            else:
                l = m + 1

        return l

    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        r = len(grid[0])
        for row in range(len(grid)):
            i = self._binary_search(grid[row], 0, r)
            r = min(i + 1, len(grid[0]))
            ret += len(grid[row]) - i

        return ret
