# https://leetcode.com/problems/daily-temperatures/
# 739. Daily Temperatures

# History:
# Apple
# 1.
# May 20, 2019
# 2.
# Nov 22, 2019
# 3.
# Mar 21, 2020

# Given a list of daily temperatures T, return a list such that, for each
# day in the input, tells you how many days you would have to wait until a
# warmer temperature. If there is no future day for which this is possible,
# put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72,
# 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each
# temperature will be an integer in the range [30, 100].


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and stack[-1][0] < T[i]:
                lst = stack.pop()
                ret[lst[1]] = i - lst[1]
            stack.append((T[i], i))

        return ret
