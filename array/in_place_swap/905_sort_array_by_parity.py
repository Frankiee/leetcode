# [In-Place-Swap]
# https://leetcode.com/problems/sort-array-by-parity/
# 905. Sort Array By Parity

# History:
# 1.
# Aug 25, 2019
# 2.
# Nov 23, 2019

# Given an array A of non-negative integers, return an array consisting of
# all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
# Note:
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = 0

        for curr in range(len(A)):
            if A[curr] % 2 == 0:
                A[l], A[curr] = A[curr], A[l]
                l += 1

        return A
