# [Archived]
# https://leetcode.com/problems/plus-one/
# 66. Plus One

# History:
# Google
# 1.
# Mar 10, 2020

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            curr_sum = digits[i] + carry
            if i == len(digits) - 1:
                curr_sum += 1
            curr_digit = curr_sum % 10
            carry = curr_sum / 10
            digits[i] = curr_digit

        if carry > 0:
            digits.insert(0, carry)

        return digits
