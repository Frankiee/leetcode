# https://leetcode.com/problems/different-ways-to-add-parentheses/
# 241. Different Ways to Add Parentheses

# History:
# 1.
# Apr 15, 2019
# 2.
# Nov 23, 2019

# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators.
# The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10


class Solution(object):
    def __init__(self):
        self.cache = {}

    def tokenize(self, input):
        ret = []
        curr_num = 0

        for c in input:
            if c in {'+', '-', '*'}:
                ret.append(curr_num)
                ret.append(c)
                curr_num = 0
            else:
                curr_num = curr_num * 10 + int(c)

        ret.append(curr_num)

        return ret

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = self.tokenize(input)

        return self.diff_ways_to_compute(tokens, 0, len(tokens))

    def diff_ways_to_compute(self, tokens, l, r):
        if (l, r) in self.cache:
            return self.cache[(l, r)]

        if r - l == 1:
            self.cache[(l, r)] = [tokens[l]]
            return [tokens[l]]

        ret = []
        for op in range(l + 1, r, 2):
            lefts = self.diff_ways_to_compute(tokens, l, op)
            rights = self.diff_ways_to_compute(tokens, op + 1, r)

            for left in lefts:
                for right in rights:
                    if tokens[op] == '+':
                        ret.append(left + right)
                    elif tokens[op] == '-':
                        ret.append(left - right)
                    else:
                        ret.append(left * right)

        self.cache[(l, r)] = ret
        return ret
