# https://leetcode.com/problems/additive-number/
# 306. Additive Number


# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the
# sum of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199.
#              1 + 99 = 100, 99 + 100 = 199


class Solution(object):
    def is_additive_number(self, num1, num2, rest):
        if ((num1[0] == '0' and len(num1) > 1) or
                (num2[0] == '0' and len(num2) > 1)):
            return False

        while rest:
            num1, num2 = int(num1), int(num2)
            next_num = str(num1 + num2)
            if len(rest) < len(next_num):
                return False
            if rest[0:len(next_num)] != next_num:
                return False
            num1 = num2
            num2 = int(next_num)
            rest = rest[len(next_num):]

        return True

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False

        len1 = len2 = 1

        for len1 in range(1, len(num) / 2 + 2):
            for len2 in range(1, min(len(num) - 2 * len1 + 1,
                                     len(num) - len1 + 1)):
                if self.is_additive_number(num[0:len1], num[len1:len1 + len2],
                                           num[len1 + len2:]):
                    return True
        return False
