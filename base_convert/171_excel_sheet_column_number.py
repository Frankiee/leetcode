# https://leetcode.com/problems/excel-sheet-column-number/
# 171. Excel Sheet Column Number

# History:
# Facebook
# 1.
# May 8, 2020

# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701


class Solution(object):
    BASE = ord('A')

    def _to_digit(self, c):
        return ord(c) - self.BASE + 1

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0

        for c in s:
            ret *= 26
            ret += self._to_digit(c)

        return ret
