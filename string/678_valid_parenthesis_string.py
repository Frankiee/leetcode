# [Classic]
# https://leetcode.com/problems/valid-parenthesis-string/
# 678. Valid Parenthesis String

# History:
# Facebook
# 1.
# Mar 2, 2020
# 2.
# Apr 30, 2020

# Given a string containing only three types of characters: '(', ')' and '*', write a function to
# check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an
# empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].


# Optimal O(n)
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c_min, c_max = 0, 0

        for c in s:
            if c == '(':
                c_min += 1
                c_max += 1
            elif c == ')':
                c_min -= 1
                c_max -= 1

                c_min = max(0, c_min)
            else:
                c_min -= 1
                c_min = max(0, c_min)

                c_max += 1

            if c_max < 0:
                return False

        return c_min <= 0 <= c_max


class SolutionDFS(object):
    def _dfs(self, parenthesis_balance, s, curr_idx):
        if curr_idx == len(s):
            return parenthesis_balance == 0

        if s[curr_idx] == '(':
            return self._dfs(parenthesis_balance + 1, s, curr_idx + 1)
        elif s[curr_idx] == ')':
            if parenthesis_balance <= 0:
                return False
            return self._dfs(parenthesis_balance - 1, s, curr_idx + 1)
        elif s[curr_idx] == '*':
            # (
            if self._dfs(parenthesis_balance + 1, s, curr_idx + 1):
                return True
            # )
            if parenthesis_balance > 0 and self._dfs(parenthesis_balance - 1, s, curr_idx + 1):
                return True
            # empty string
            return self._dfs(parenthesis_balance, s, curr_idx + 1)

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._dfs(0, s, 0)
