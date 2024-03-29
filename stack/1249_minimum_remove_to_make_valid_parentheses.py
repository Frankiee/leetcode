# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 1249. Minimum Remove to Make Valid Parentheses

# History:
# Facebook
# 1.
# Dec 14, 2019
# 2.
# Feb 3, 2020
# 3.
# Apr 22, 2020

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so
# that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        ret = []
        for c in s:
            if c == '(':
                stack.append(len(ret))
                ret.append(c)
            elif c == ')':
                if stack:
                    stack.pop(-1)
                    ret.append(c)
            else:
                ret.append(c)

        for i in stack:
            ret[i] = ''

        return "".join(ret)
