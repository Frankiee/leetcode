# https://leetcode.com/problems/excel-sheet-column-title/
# 168. Excel Sheet Column Title

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


class Solution(object):
    def to_ascii(self, num):
        return str(unichr(num + 65))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n:
            next_digit = (n - 1) % 26
            ret.insert(0, self.to_ascii(next_digit))
            n = (n - 1) / 26

        return ''.join(ret)
