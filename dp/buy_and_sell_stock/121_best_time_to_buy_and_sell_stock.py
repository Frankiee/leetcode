# [Buy-And-Sell-Stock]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock

# History:
# Apple
# 1.
# Feb 3, 2019
# 2.
# Nov 23, 2019
# 3.
# Mar 7, 2020
# 4.
# Apr 28, 2020

# Say you have an array for which the ith element is the price of a given
# stock on day i.

# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
# profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        profit = 0

        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)

        return profit


# Think as finite state machine
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_state = float('-inf')
        sell_state = 0

        for p in prices:
            buy_state = max(buy_state, -p)
            sell_state = max(sell_state, p + buy_state)

        return sell_state
