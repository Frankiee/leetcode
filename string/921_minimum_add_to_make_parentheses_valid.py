# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# 921. Minimum Add to Make Parentheses Valid

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 22, 2020
# 3.
# May 12, 2020

# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or
# ')', and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the
# resulting string valid.
#
#
#
# Example 1:
#
# Input: "())"
# Output: 1
# Example 2:
#
# Input: "((("
# Output: 3
# Example 3:
#
# Input: "()"
# Output: 0
# Example 4:
#
# Input: "()))(("
# Output: 4
#
#
# Note:
#
# S.length <= 1000
# S only consists of '(' and ')' characters.


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        balance = 0

        for c in S:
            if c == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ret += 1

        ret += balance
        return ret
