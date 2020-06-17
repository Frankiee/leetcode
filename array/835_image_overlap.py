# [Classic]
# https://leetcode.com/problems/image-overlap/
# 835. Image Overlap

# History:
# Google
# 1.
# Mar 10, 2020

# Two images A and B are given, represented as binary, square matrices of the same size.  (A
# binary matrix has only 0s and 1s as values.)
#
# We translate one image however we choose (sliding it left, right, up, or down any number of
# units), and place it on top of the other image.  After, the overlap of this translation is the
# number of positions that have a 1 in both images.
#
# (Note also that a translation does not include any kind of rotation.)
#
# What is the largest possible overlap?
#
# Example 1:
#
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes:
#
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1


from collections import defaultdict


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        a_ones = []
        b_ones = []

        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    a_ones.append((r, c))
                if B[r][c] == 1:
                    b_ones.append((r, c))

        ret = 0
        freq = defaultdict(int)
        for a_one in a_ones:
            for b_one in b_ones:
                key = str(a_one[0] - b_one[0]) + '|' + str(a_one[1] - b_one[1])
                freq[key] += 1
                ret = max(ret, freq[key])

        return ret
