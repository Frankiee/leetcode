# https://leetcode.com/problems/multiply-strings/
# 43. Multiply Strings

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 11, 2020
# 3.
# May 8, 2020

# Given two non-negative integers num1 and num2 represented as strings, return the product of
# num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        for num1_shift in range(len(num1)):
            for num2_shift in range(len(num2)):
                shift = num1_shift + num2_shift

                if shift > len(ret) - 1:
                    ret.append(0)

                ret[shift] += int(num1[-(num1_shift + 1)]) * int(num2[-(num2_shift + 1)])

        idx = 0
        carry = 0
        while idx < len(ret) or carry:
            nxt_sum = carry
            if idx < len(ret):
                nxt_sum += ret[idx]

            if idx >= len(ret):
                ret.append(0)
            ret[idx] = str(nxt_sum % 10)
            carry = nxt_sum / 10

            idx += 1

        return str(int("".join(ret[::-1])))


class SolutionLastDigit(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]

        ret = []
        for num1_shift in range(len(num1)):
            for num2_shift in range(len(num2)):
                shift = num1_shift + num2_shift
                if len(ret) - 1 < shift:
                    ret.append(0)
                ret[shift] += int(num1[num1_shift]) * int(num2[num2_shift])

        ret.append(0)
        carry = 0
        last_digit = 0
        for i in range(len(ret)):
            num = ret[i] + carry
            ret[i] = str(num % 10)
            carry = num / 10
            if ret[i] != '0':
                last_digit = i

        return "".join(ret[:last_digit + 1][::-1])
