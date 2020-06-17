# [Matrix]
# https://leetcode.com/problems/diagonal-traverse/
# 498. Diagonal Traverse

# History:
# Facebook
# 1.
# Mar 27, 2020
# 2.
# Apr 9, 2020
# 3.
# May 8, 2020

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
# diagonal order as shown in the below image.
#
#
#
# Example:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.


class SolutionTrackMovement(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        r, c = 0, 0

        ret = []
        while True:
            ret.append(matrix[r][c])
            if (r + c) % 2 == 0:
                r -= 1
                c += 1
            else:
                r += 1
                c -= 1

            if c == len(matrix[0]):
                r += 2
                c -= 1
            elif r == -1:
                r += 1
            elif r == len(matrix):
                c += 2
                r -= 1
            elif c == -1:
                c += 1

            if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
                return ret


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        ret = []
        direction = 1
        for s in range(len(matrix) + len(matrix[0])):
            if direction == 1:
                for r in range(min(s, len(matrix) - 1), -1, -1):
                    c = s - r
                    if c >= len(matrix[0]):
                        break
                    ret.append(matrix[r][c])
            else:
                for c in range(min(s, len(matrix[0]) - 1), -1, -1):
                    r = s - c
                    if r >= len(matrix):
                        break
                    ret.append(matrix[r][c])

            direction = 0 if direction == 1 else 1

        return ret


class SolutionReverse(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        ret = []

        direction = 0
        for total in range(len(matrix) + len(matrix[0]) - 1):
            r = min(total, len(matrix) - 1)
            c = total - r

            row = []
            while True:
                if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
                    break
                row.append(matrix[r][c])
                r -= 1
                c += 1

            if direction == 1:
                row = row[::-1]
            direction = 0 if direction == 1 else 1
            ret.extend(row)

        return ret
