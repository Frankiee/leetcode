# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 417. Pacific Atlantic Water Flow

# History:
# Google, Facebook
# 1.
# Mar 25, 2020
# 2.
# May 2, 2020

# Given an m x n matrix of non-negative integers representing the height of each unit cell in a
# continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic
# ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one
# with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
#
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above
# matrix).


class SolutionBFS(object):
    def _bfs(self, matrix, to_do):
        visited = set()

        while to_do:
            next_to_do = set()

            for r, c in to_do:
                visited.add((r, c))

                for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (0 <= n_r < len(matrix) and
                            0 <= n_c < len(matrix[0]) and
                            (n_r, n_c) not in visited and
                            matrix[n_r][n_c] >= matrix[r][c]):
                        next_to_do.add((n_r, n_c))

            to_do = next_to_do

        return visited

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        pacific_to_do, atlantic_to_do = set(), set()

        for r in range(len(matrix)):
            pacific_to_do.add((r, 0))
            atlantic_to_do.add((r, len(matrix[0]) - 1))

        for c in range(len(matrix[0])):
            pacific_to_do.add((0, c))
            atlantic_to_do.add((len(matrix) - 1, c))

        atlantic_visited = self._bfs(matrix, atlantic_to_do)
        pacific_visited = self._bfs(matrix, pacific_to_do)

        return atlantic_visited.intersection(pacific_visited)


class SolutionQueue(object):
    def _get_coordinates(self, matrix, to_do):
        ret = to_do.copy()

        while to_do:
            r, c = to_do.pop()

            for n_r, n_c in [[r + 1, c], [r - 1, c], [r, c - 1], [r, c + 1]]:
                if 0 <= n_r < len(matrix) and 0 <= n_c < len(matrix[0]) and (
                n_r, n_c) not in ret and matrix[n_r][n_c] >= matrix[r][c]:
                    ret.add((n_r, n_c))
                    to_do.add((n_r, n_c))

        return ret

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        pacific, atlantic = set(), set()

        for r in range(len(matrix)):
            pacific.add((r, 0))
            atlantic.add((r, len(matrix[0]) - 1))

        for c in range(len(matrix[0])):
            pacific.add((0, c))
            atlantic.add((len(matrix) - 1, c))

        pacific = self._get_coordinates(matrix, pacific)
        atlantic = self._get_coordinates(matrix, atlantic)

        return list(pacific.intersection(atlantic))
