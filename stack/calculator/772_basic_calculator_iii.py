# [Calculator, Classic]
# https://leetcode.com/problems/basic-calculator-iii/
# 772. Basic Calculator III

# https://www.youtube.com/watch?v=vq-nUF0G4fI

# History:
# Google
# 1.
# Jan 3, 2020

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
# non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and
# closing parentheses ) and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in
# the range of [-2147483648, 2147483647].
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12


class Solution(object):
    def tokenize(self, s):
        ret = []

        sign = 1
        num = None
        for c in s:
            if c == ' ':
                pass
            elif c in ['+', '-']:
                if num is not None:
                    ret.append(num if sign == 1 else -num)
                num = None
                sign = 1

                if c == '-' and not ret or ret[-1] in ['(', '*', '/']:
                    sign = -1
                else:
                    ret.append(c)
            elif c in ['(', ')', '*', '/']:
                if num is not None:
                    ret.append(num if sign == 1 else -num)
                num = None
                sign = 1

                ret.append(c)
            else:
                if num is None:
                    num = int(c)
                else:
                    num *= 10
                    num += int(c)

        if num is not None:
            ret.append(num if sign == 1 else -num)

        return ret

    def infix_to_postfix(self, tokens):
        stack = []
        postfix = []

        for t in tokens:
            if isinstance(t, int):
                postfix.append(t)
            elif t == '(':
                stack.append(t)
            elif t in ['*', '/']:
                while stack and stack[-1] in ['*', '/']:
                    postfix.append(stack.pop())
                stack.append(t)
            elif t in ['+', '-']:
                while stack and stack[-1] in ['*', '/', '+', '-']:
                    postfix.append(stack.pop())
                stack.append(t)
            else:
                # ')'
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

        while stack:
            postfix.append(stack.pop())

        return postfix

    def evaluate_postfix(self, postfix):
        stack = []

        for t in postfix:
            if isinstance(t, int):
                stack.append(t)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if t == '+':
                    res = operand1 + operand2
                elif t == '-':
                    res = operand1 - operand2
                elif t == '*':
                    res = operand1 * operand2
                elif t == '/':
                    res = operand1 / operand2

                stack.append(res)

        return stack[-1]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = self.tokenize(s)

        postfix = self.infix_to_postfix(tokens)

        return self.evaluate_postfix(postfix)
