# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses

# History:
# 1.
# Apr 21, 2019
# 2.
# Nov 12, 2019
# 3.
# Apr 3, 2020
# 4.
# Apr 22, 2020

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
    PAIRS = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c not in self.PAIRS:
                stack.append(c)
            else:
                if not stack or stack.pop(-1) != self.PAIRS[c]:
                    return False

        return not stack
