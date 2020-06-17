# [Classic, 0-1-Knapsack, Knapsack]
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# 0-1 Knapsack Problem

# History:
# 1.
# Dec 17, 2019

# Given weights and values of n items, put these items in a
# knapsack of capacity W to get the maximum total value in the knapsack.
# In other words, given two integer arrays val[0..n-1] and
# wt[0..n-1] which represent values and weights associated with n
# items respectively. Also given an integer W which represents knapsack
# capacity, find out the maximum value subset of val[]
# such that sum of the weights of this subset is smaller than or equal
# to W. You cannot break an item, either pick the complete item,
# or don't pick it (0-1 property).


class Solution(object):
    def get_max_weight(self, values, weights, W):
        dp = [None] * len(values)

        for r in range(len(values)):
            dp[r] = [None] * (W + 1)

        for idx in range(len(values)):
            for w in range(W + 1):
                if idx == 0:
                    dp[idx][w] = values[idx] if weights[idx] <= w else 0
                else:
                    dp[idx][w] = max(
                        dp[idx-1][w],
                        values[idx] + dp[idx-1][w-weights[idx]] if w >= weights[idx] else 0,
                    )

        return dp[len(values)-1][w]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
solution = Solution()

print solution.get_max_weight(values, weights, W)
