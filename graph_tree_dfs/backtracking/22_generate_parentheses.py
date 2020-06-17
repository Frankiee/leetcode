# [Backtracking, Classic]
# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 14, 2020
# 3.
# May 2, 2020

# Given n pairs of parentheses, write a function to generate all combinations of well-formed
# parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def dfs(self, left_remain, right_remain, curr, ret):
        if left_remain == 0 and right_remain == 0:
            ret.append(curr)
            return

        # left
        if left_remain > 0:
            self.dfs(left_remain - 1, right_remain, curr + '(', ret)

        # right
        if left_remain < right_remain and right_remain > 0:
            self.dfs(left_remain, right_remain - 1, curr + ')', ret)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        self.dfs(n, n, "", ret)

        return ret
