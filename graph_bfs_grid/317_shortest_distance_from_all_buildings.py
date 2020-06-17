# [Classic]
# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# 317. Shortest Distance from All Buildings

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# May 15, 2020

# You want to build a house on an empty land which reaches all buildings in the shortest amount
# of distance. You can only move up, down, left and right. You are given a 2D grid of values 0,
# 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# Example:
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 7
#
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total
#              travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building. If it is not possible to build such house according to the
# above rules, return -1.


from collections import defaultdict


class SolutionVisitedCount(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        buildings = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    buildings.append((r, c))

        distance = defaultdict(int)
        reach_count = defaultdict(int)
        for r, c in buildings:
            visited = set()

            d = 0
            to_do = [(r, c)]
            visited.add((r, c))
            while to_do:
                nxt_to_do = []

                for t_r, t_c in to_do:
                    if grid[t_r][t_c] == 0:
                        distance[(t_r, t_c)] += d
                        reach_count[(t_r, t_c)] += 1
                    for n_r, n_c in [(t_r + 1, t_c), (t_r - 1, t_c), (t_r, t_c + 1),
                                     (t_r, t_c - 1)]:
                        if (0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and
                                grid[n_r][n_c] == 0 and (n_r, n_c) not in visited):
                            visited.add((n_r, n_c))
                            nxt_to_do.append((n_r, n_c))

                d += 1
                to_do = nxt_to_do

        ret = float('inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if reach_count[(r, c)] == len(buildings):
                    ret = min(ret, distance[(r, c)])

        return -1 if ret == float('inf') else ret


from collections import defaultdict


class Solution1(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        to_do = {}
        mp = defaultdict(dict)

        i = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    to_do[i] = [(r, c)]
                    i += 1

        building_count = len(to_do)

        ret = float('inf')
        distance = 1
        while to_do:
            nxt_to_do = {}

            for i, i_to_do in to_do.iteritems():
                i_nxt_to_do = []

                for r, c in i_to_do:
                    for n_r, n_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                        if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] == 0:
                            if i not in mp[(n_r, n_c)]:
                                mp[(n_r, n_c)][i] = distance
                                i_nxt_to_do.append((n_r, n_c))

                                if len(mp[(n_r, n_c)]) == building_count:
                                    ret = min(ret, sum(mp[(n_r, n_c)].values()))

                if i_nxt_to_do:
                    nxt_to_do[i] = i_nxt_to_do

            to_do = nxt_to_do
            distance += 1

        return -1 if ret == float('inf') else ret


class Solution2(object):
    def _dfs(self, grid, r, c, houses, reachable_so_far):
        to_do = [(r, c)]
        visited = set()
        distance = 0

        min_distance = float('inf')

        while to_do:
            next_to_do = []

            for r, c in to_do:
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                grid[r][c] += distance
                if (0 < grid[r][c] < min_distance and (
                    reachable_so_far is None or (r, c) in reachable_so_far)):
                    min_distance = grid[r][c]

                for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]):
                        if grid[n_r][n_c] == -1:
                            visited.add((n_r, n_c))

                        if grid[n_r][n_c] >= 0 and (n_r, n_c) not in visited:
                            next_to_do.append((n_r, n_c))

            to_do = next_to_do
            distance += 1

        reachable_so_far = (
            visited.intersection(reachable_so_far) if reachable_so_far is not None else visited)
        return min_distance if all(
            h == (r, c) or h in visited for h in houses) and min_distance != float(
            'inf') else -1, reachable_so_far

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        to_do = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    to_do.append((r, c))
                if grid[r][c] != 0:
                    grid[r][c] = - grid[r][c]

        min_distance = -1
        reachable_so_far = None
        for r, c in to_do:
            min_distance, reachable_so_far = self._dfs(grid, r, c, to_do, reachable_so_far)

            if min_distance == -1:
                return -1

        return min_distance
