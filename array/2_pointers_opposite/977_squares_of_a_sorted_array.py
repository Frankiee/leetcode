# [2-Pointers-Opposite]
# https://leetcode.com/problems/squares-of-a-sorted-array/
# 977. Squares of a Sorted Array

# History:
# 1.
# Facebook
# Dec 17, 2019
# 2.
# Mar 27, 2020
# 3.
# Apr 12, 2020
# 4.
# Apr 26, 2020

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of
# each number, also in sorted non-decreasing order.
#
#
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(A) - 1

        ret = []

        while l <= r:
            if A[l] ** 2 < A[r] ** 2:
                ret.append(A[r] ** 2)
                r -= 1
            else:
                ret.append(A[l] ** 2)
                l += 1

        return ret[::-1]
