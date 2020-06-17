# [Stack-Monotone, Classic]
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram

# History:
# Cruise
# 1.
# May 17, 2020

# Given n non-negative integers representing the histogram's bar height where the width of each
# bar is 1, find the area of largest rectangle in the histogram.
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ret = 0

        for i, curr_h in enumerate(heights):
            while stack and heights[stack[-1]] > curr_h:
                pre_h_idx = stack.pop(-1)
                h = heights[pre_h_idx]
                w = i - stack[-1] - 1
                ret = max(ret, h * w)

            stack.append(i)

        return ret
