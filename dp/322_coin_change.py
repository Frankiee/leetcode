# [Important]
# https://leetcode.com/problems/coin-change/
# 322. Coin Change

# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you
# need to make up that amount. If that amount of money cannot be made up by
# any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)

        for i in range(amount + 1):
            for c in coins:
                if c == i:
                    dp[i] = 1
                    break

                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]
