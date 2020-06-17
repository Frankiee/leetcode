# https://leetcode.com/problems/add-binary/
# 67. Add Binary

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 22, 2020

# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        a_i, b_i = len(a) - 1, len(b) - 1

        ret = []
        while a_i >= 0 or b_i >= 0 or carry:
            nxt = carry
            if a_i >= 0:
                nxt += int(a[a_i])
                a_i -= 1
            if b_i >= 0:
                nxt += int(b[b_i])
                b_i -= 1

            ret.append(str(nxt % 2))
            carry = nxt / 2

        return "".join(ret[::-1])
