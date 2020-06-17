# [Backtracking, Classic]
# https://leetcode.com/problems/remove-invalid-parentheses/
# 301. Remove Invalid Parentheses

# History:
# Facebook
# 1.
# Feb 3, 2020
# 2.
# Apr 22, 2020

# Remove the minimum number of invalid parentheses in order to make the input string valid.
# Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]


class Solution(object):
    def _dfs(self, s, i, balance, left_to_remove, right_to_remove, curr, ret):
        if i == len(s):
            if left_to_remove == right_to_remove == balance == 0:
                ret.append(curr)
            return

        if s[i] == '(':
            if left_to_remove > 0 and (not curr or curr[-1] != '('):
                self._dfs(s, i + 1, balance, left_to_remove - 1, right_to_remove, curr, ret)
            self._dfs(s, i + 1, balance + 1, left_to_remove, right_to_remove, curr + '(', ret)
        elif s[i] == ')':
            if right_to_remove > 0 and (not curr or curr[-1] != ')'):
                self._dfs(s, i + 1, balance, left_to_remove, right_to_remove - 1, curr, ret)
            if balance > 0:
                self._dfs(s, i + 1, balance - 1, left_to_remove, right_to_remove, curr + ')', ret)
        else:
            self._dfs(s, i + 1, balance, left_to_remove, right_to_remove, curr + s[i], ret)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        balance = left_to_remove = right_to_remove = 0

        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                if balance > 0:
                    balance -= 1
                else:
                    right_to_remove += 1

        left_to_remove = balance

        ret = []

        self._dfs(s, 0, 0, left_to_remove, right_to_remove, "", ret)

        return ret
