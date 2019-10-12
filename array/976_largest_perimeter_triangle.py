# [Triangle]
# https://leetcode.com/problems/largest-perimeter-triangle/
# 976. Largest Perimeter Triangle

# Given an array A of positive lengths, return the largest perimeter of a
# triangle with non-zero area, formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0.
#
# Example 1:
#
# Input: [2,1,2]
# Output: 5
#
# Example 2:
#
# Input: [1,2,1]
# Output: 0
#
# Example 3:
#
# Input: [3,2,3,4]
# Output: 10
#
# Example 4:
#
# Input: [3,6,2,3]
# Output: 8
#
#
# Note:
#
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        sorted_a = sorted(A, reverse=True)

        for i in range(len(A) - 2):
            print i, A[i], A[i + 1] + A[i + 2]
            if sorted_a[i] < sorted_a[i + 1] + sorted_a[i + 2]:
                return sorted_a[i] + sorted_a[i + 1] + sorted_a[i + 2]

        return 0
