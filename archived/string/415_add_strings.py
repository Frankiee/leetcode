# [Archived]
# https://leetcode.com/problems/add-strings/
# 415. Add Strings

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 24, 2020

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and
# num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1_p, n2_p = len(num1) - 1, len(num2) - 1

        carry = 0
        ret = []
        while n1_p >= 0 or n2_p >= 0 or carry:
            nxt = carry

            if n1_p >= 0:
                nxt += int(num1[n1_p])
                n1_p -= 1
            if n2_p >= 0:
                nxt += int(num2[n2_p])
                n2_p -= 1

            ret.append(str(nxt % 10))
            carry = nxt / 10

        return "".join(ret[::-1])
