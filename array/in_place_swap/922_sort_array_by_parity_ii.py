# [InPlaceSwap]
# https://leetcode.com/problems/sort-array-by-parity-ii/
# 922. Sort Array By Parity II

# Given an array A of non-negative integers, half of the integers in A are
# odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i]
# is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
# Note:
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A

        even_p = 0
        odd_p = 1

        while odd_p < len(A) and even_p < len(A) - 1:
            if A[even_p] % 2 == 0 and A[odd_p] % 2 == 1:
                even_p += 2
                odd_p += 2
            elif A[even_p] % 2 == 1:
                A[even_p], A[odd_p] = A[odd_p], A[even_p]
                odd_p += 2
            else:
                A[even_p], A[odd_p] = A[odd_p], A[even_p]
                even_p += 2

        return A
