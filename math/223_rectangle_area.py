# https://leetcode.com/problems/rectangle-area/
# 223. Rectangle Area

# History:
# Facebook
# 1.
# Mar 2, 2020
# 2.
# May 8, 2020

# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
#
# Example:
#
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Note:
#
# Assume that the total area is never beyond the maximum possible value of int.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left_bottom_x = max(A, E)
        left_bottom_y = max(B, F)

        right_top_x = min(C, G)
        right_top_y = min(D, H)

        overlap = max(0, right_top_x - left_bottom_x) * max(0, right_top_y - left_bottom_y)

        return (C - A) * (D - B) + (G - E) * (H - F) - overlap
