# [Archived]
# https://leetcode.com/problems/pascals-triangle/
# 118. Pascal's Triangle

# History:
# Facebook
# 1.
# Sep 9, 2019
# 2.
# Mar 7, 2020
# 3.
# Apr 8, 2020

# Given a non-negative integer numRows, generate the first numRows of
# Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        ret = [[1]]

        for r in range(2, numRows + 1):
            pre = ret[-1]

            new_row = [1]
            for idx in range(1, len(pre)):
                new_row.append(pre[idx] + pre[idx - 1])
            new_row.append(1)
            ret.append(new_row)

        return ret
