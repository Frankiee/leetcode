# [Classic]
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 329. Longest Increasing Path in a Matrix

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 23, 2020

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT
# move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


class Solution(object):
    def _get_longest_path(self, matrix, r, c, mem):
        if (r, c) in mem:
            return mem[(r, c)]

        ret = 1
        for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (0 <= n_r < len(matrix) and 0 <= n_c < len(matrix[0]) and
                    matrix[r][c] > matrix[n_r][n_c]):
                ret = max(ret, 1 + self._get_longest_path(matrix, n_r, n_c, mem))

        mem[(r, c)] = ret
        return ret

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        mem = {}
        ret = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ret = max(ret, self._get_longest_path(matrix, r, c, mem))

        return ret
