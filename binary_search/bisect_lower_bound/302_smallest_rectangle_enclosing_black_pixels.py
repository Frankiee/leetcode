# [Bisect-Lower-Bound]
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/
# 302. Smallest Rectangle Enclosing Black Pixels

# History:
# Netflix
# 1.
# Jun 8, 2020

# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The
# black pixels are connected, i.e., there is only one black region. Pixels are connected
# horizontally and vertically. Given the location (x, y) of one of the black pixels, return the
# area of the smallest (axis-aligned) rectangle that encloses all black pixels.
#
# Example:
#
# Input:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2
#
# Output: 6


class Solution(object):
    def _search_up(self, image, l, r):
        while l < r:
            m = (r - l) / 2 + l

            if '1' in image[m]:
                r = m
            else:
                l = m + 1

        return l

    def _search_down(self, image, l, r):
        while l < r:
            m = (r - l) / 2 + l

            if '1' not in image[m]:
                r = m
            else:
                l = m + 1

        return l

    def _search_left(self, image, l, r):
        while l < r:
            m = (r - l) / 2 + l

            if any([image[row][m] == '1' for row in range(len(image))]):
                r = m
            else:
                l = m + 1

        return l

    def _search_right(self, image, l, r):
        while l < r:
            m = (r - l) / 2 + l

            if all([image[row][m] == '0' for row in range(len(image))]):
                r = m
            else:
                l = m + 1

        return l

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        up = self._search_up(image, 0, x + 1)
        down = self._search_down(image, x, len(image))
        left = self._search_left(image, 0, y + 1)
        right = self._search_right(image, y, len(image[0]))

        return (right - left) * (down - up)
