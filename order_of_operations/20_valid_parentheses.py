# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if (c == ')' and top != '(' or
                    c == '}' and top != '{' or
                    c == ']' and top != '['):
                    return False
                stack.pop()

        return not stack