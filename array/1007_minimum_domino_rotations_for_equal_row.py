# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# 1007. Minimum Domino Rotations For Equal Row

# History:
# Google
# 1.
# Mar 9, 2020

# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A
# domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
#
# Return the minimum number of rotations so that all the values in A are the same, or all the
# values in B are the same.
#
# If it cannot be done, return -1.
#
#
#
# Example 1:
#
#
#
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
# as indicated by the second figure.
# Example 2:
#
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
#
#
# Note:
#
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) != len(B):
            return -1

        possibles = set()
        for i in range(len(A)):
            if i == 0:
                possibles = {A[0], B[0]}
            else:
                possibles = possibles.intersection(
                    {A[i], B[i]}
                )

        if len(possibles) == 0:
            return -1

        common_num = possibles.pop()

        ret_a, ret_b = 0, 0
        for i in range(len(A)):
            if A[i] != common_num:
                ret_a += 1
            if B[i] != common_num:
                ret_b += 1

        return min(ret_a, len(A) - ret_a, ret_b, len(A) - ret_b)
