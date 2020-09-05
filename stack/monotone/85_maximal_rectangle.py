# [Stack-Monotone, Classic]
# https://leetcode.com/problems/maximal-rectangle/
# 85. Maximal Rectangle

# History:
# Google
# 1.
# Jun 16, 2020

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only
# 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        heights = [0] * (len(matrix[0]) + 1)
        ret = 0

        for row in matrix:
            for c in range(len(matrix[0])):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0

            stack = [-1]
            for i, curr_h in enumerate(heights):
                while stack and heights[stack[-1]] > curr_h:
                    pre_h_idx = stack.pop(-1)
                    h = heights[pre_h_idx]
                    w = i - stack[-1] - 1
                    ret = max(ret, w * h)
                stack.append(i)

        return ret
