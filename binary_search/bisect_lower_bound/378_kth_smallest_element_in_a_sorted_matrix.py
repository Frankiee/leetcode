# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.

import bisect


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = matrix[0][0]
        r = matrix[-1][-1] + 1

        while l < r:
            m = l + (r - l) / 2

            total = 0  # total # of elements <= m
            for row in matrix:
                total += bisect.bisect_right(row, m)

            # Minimal m so that total >= k
            if total >= k:
                r = m
            else:
                l = m + 1

        return l
