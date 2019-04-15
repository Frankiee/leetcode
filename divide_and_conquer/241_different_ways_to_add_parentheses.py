# https://leetcode.com/problems/different-ways-to-add-parentheses/
# 241. Different Ways to Add Parentheses

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
        self.dp = {}

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in self.dp:
            return self.dp[input]

        has_operator = False
        ret = []
        for i in range(len(input)):
            if input[i] in {'+', '-', '*'}:
                has_operator = True
                left_ret = self.diffWaysToCompute(input[0:i])
                right_ret = self.diffWaysToCompute(input[i + 1:])

                for l in left_ret:
                    for r in right_ret:
                        l = int(l)
                        r = int(r)
                        if input[i] == '+':
                            ret.append(l + r)
                        elif input[i] == '-':
                            ret.append(l - r)
                        else:
                            ret.append(l * r)

                self.dp[input] = ret

        if not has_operator:
            ret = [int(input)]
            self.dp[input] = ret
            return ret

        return ret
