# https://leetcode.com/problems/excel-sheet-column-title/
# 168. Excel Sheet Column Title

# History:
# Facebook
# 1.
# Mar 19, 2019
# 2.
# May 11, 2020

# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"


from collections import deque


class Solution(object):
    def _convert_to_char(self, num):
        return str(unichr(num + 65))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = deque()
        while n:
            n -= 1
            nxt_c = self._convert_to_char(n % 26)

            ret.appendleft(nxt_c)
            n /= 26

        return "".join(ret)
