# [Classic, BFS, DFS, Queue]
# https://leetcode.com/problems/shortest-bridge/
# 934. Shortest Bridge

# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to
# form 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
#
# Example 1:
#
# Input: [[0,1],[1,0]]
# Output: 1
#
# Example 2:
#
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#
# Example 3:
#
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
# Note:
#
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1

# BFS
class SolutionBFS(object):
    def _expand_first_island_mark(self, A, r, c, to_do):
        if A[r][c] != 1:
            return

        A[r][c] = 2

        for d_r, d_c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_r = r + d_r
            new_c = c + d_c
            if 0 <= new_r < len(A) and 0 <= new_c < len(A[0]):
                if A[new_r][new_c] == 0:
                    to_do.add((new_r, new_c))
                elif A[new_r][new_c] == 1:
                    self._expand_first_island_mark(A, new_r, new_c, to_do)

    def _find_first_island_mark(self, A, to_do):
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    self._expand_first_island_mark(A, r, c, to_do)
                    return

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        to_do = set()
        self._find_first_island_mark(A, to_do)

        round = 0
        new_do_do = set()
        while to_do:
            for r, c in to_do:
                if A[r][c] == 1:
                    return round
                A[r][c] = 2
                for d_r, d_c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_r = r + d_r
                    new_c = c + d_c
                    if 0 <= new_r < len(A) and 0 <= new_c < len(A[0]):
                        if A[new_r][new_c] in [0, 1]:
                            new_do_do.add((new_r, new_c))

            to_do = new_do_do
            round += 1
            new_do_do = set()


# DFS
class SolutionDFS(object):
    def _find_first_island(self, A, row_count, column_count):
        # find first island
        for r in range(row_count):
            for c in range(column_count):
                if A[r][c] == 1:
                    return r, c

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row_count = len(A)
        column_count = len(A[0])

        r, c = self._find_first_island(A, row_count, column_count)

        to_check = [(r, c)]
        A[r][c] = 2
        to_visit = []

        while to_check:
            r, c = to_check.pop(0)

            to_add = False
            for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= n_r < len(A) and 0 <= n_c < len(A[0]):
                    if A[n_r][n_c] == 1:
                        A[n_r][n_c] = 2
                        to_check.append((n_r, n_c))
                    if A[n_r][n_c] == 0:
                        to_add = True

            # Add As early as possible when the item is added to to_visit
            # instead of at popping up time. This can avoid having repeated
            # item added to the to_visit queue and make a huge difference in
            # run time
            if to_add:
                # mark as added
                A[r][c] = 3
                to_visit.append((r, c))

        step = 0
        # dfs
        while to_visit:
            next_to_visit = []
            for r, c in to_visit:
                for n_r, n_c in [(r + 1, c), (r - 1, c), (r, c + 1),
                                 (r, c - 1)]:
                    if 0 <= n_r < len(A) and 0 <= n_c < len(A[0]):
                        if A[n_r][n_c] == 1:
                            return step
                        if A[n_r][n_c] == 0:
                            A[n_r][n_c] = 3
                            next_to_visit.append((n_r, n_c))

            step += 1
            to_visit = next_to_visit
