# [Classic, Unlimited-Knapsack, Knapsack]
# https://leetcode.com/problems/coin-change-2/
# 518. Coin Change 2

# History:
# Apple
# 1.
# Mar 22, 2020
# 2.
# Apr 6, 2020

# You are given coins of different denominations and a total amount of money. Write a function to
# compute the number of combinations that make up that amount. You may assume that you have
# infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
# Note:
#
# You can assume that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[None] * (len(coins) + 1) for _ in range(amount + 1)]

        for amt in range(amount + 1):
            for coin in range(len(coins) + 1):
                if coin == 0:
                    dp[amt][coin] = (1 if amt == 0 else 0)
                else:
                    dp[amt][coin] = dp[amt][coin-1] + (dp[amt-coins[coin-1]][coin] if amt-coins[coin-1] >= 0 else 0)

        return dp[-1][-1]
