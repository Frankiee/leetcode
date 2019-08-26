# [Hard, Buy-And-Sell-Stock]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 309. Best Time to Buy and Sell Stock with Cooldown

# Say you have an array for which the ith element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown
# 1 day)
# Example:
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        sell = [float('-inf')] * len(prices)
        buy = [float('-inf')] * len(prices)
        cooldown_with_share = [float('-inf')] * len(prices)
        cooldown_without_share = [0] * len(prices)

        for p_idx in range(len(prices)):
            p = prices[p_idx]
            if p_idx == 0:
                buy[p_idx] = -p
            else:
                buy[p_idx] = cooldown_without_share[p_idx-1] - p
                sell[p_idx] = max(
                    cooldown_with_share[p_idx-1] + p,
                    buy[p_idx-1] + p
                )
                cooldown_without_share[p_idx] = max(
                    cooldown_without_share[p_idx-1],
                    sell[p_idx-1],
                )
                cooldown_with_share[p_idx] = max(
                    cooldown_with_share[p_idx-1],
                    buy[p_idx-1],
                )

        return max(
            cooldown_without_share[-1],
            buy[-1],
            sell[-1],
            cooldown_with_share[-1],
        )
