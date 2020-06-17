# [Classic]
# https://leetcode.com/problems/longest-valid-parentheses/
# 32. Longest Valid Parentheses

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# Apr 11, 2020
# 3.
# Apr 22, 2020

# Given a string containing just the characters '(' and ')', find the length of the longest valid
# (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class SolutionStack(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack and stack[-1] >= 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        stack.append(len(s))

        ret = 0
        for i in range(1, len(stack)):
            ret = max(ret, stack[i] - stack[i - 1] - 1)

        return ret


class SolutionDP(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)

        ret = 0
        for idx, c in enumerate(s):
            if c == '(':
                dp[idx] = 0
            else:
                if idx > 0:
                    if dp[idx - 1] == '(':
                        dp[idx] = 2
                        if idx > 1:
                            dp[idx] += dp[idx - 2]
                    else:
                        if idx - dp[idx - 1] - 1 >= 0 and s[idx - dp[idx - 1] - 1] == '(':
                            dp[idx] = 2 + dp[idx - 1]
                            if idx - dp[idx - 1] - 2 >= 0:
                                dp[idx] += dp[idx - dp[idx - 1] - 2]
                else:
                    dp[idx] = 0

            ret = max(ret, dp[idx])

        return ret
