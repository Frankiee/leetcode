# [Matrix-Multiplication]
# https://leetcode.com/problems/sparse-matrix-multiplication/
# 311. Sparse Matrix Multiplication

# History:
# Facebook
# 1.
# Jan 30, 2020
# 2.
# Apr 3, 2020
# 3.
# May 4, 2020

# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# Input:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
# Output:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[0] * len(B[0]) for _ in range(len(A))]

        for a_r in range(len(A)):
            for a_c in range(len(A[0])):
                if A[a_r][a_c] != 0:
                    for b_c in range(len(B[0])):
                        ret[a_r][b_c] += A[a_r][a_c] * B[a_c][b_c]

        return ret
