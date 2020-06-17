# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix

# History:
# Facebook
# 1.
# Feb 18, 2019
# 2.
# Apr 2, 2020

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


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        l, r = matrix[0][0], matrix[-1][-1] + 1

        while l < r:
            m = (r - l) / 2 + l

            count = 0
            p = n - 1
            for i in range(n):
                while p >= 0 and matrix[i][p] > m:
                    p -= 1
                count += p + 1

            if count >= k:
                r = m
            else:
                l = m + 1

        return l


import bisect


class SolutionBinarySearchBisectRight(object):
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


class SolutionBinarySearchBisectLeft(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l, r = matrix[0][0], matrix[-1][-1] + 1

        while l < r:
            m = (r - l) / 2 + l

            count = 0
            for i in range(len(matrix)):
                count += bisect.bisect(matrix[i], m)

            if count >= k:
                r = m
            else:
                l = m + 1

        return l
