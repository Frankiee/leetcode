# [Classic, Buy-And-Sell-Stock]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# 188. Best Time to Buy and Sell Stock IV

# History:
# 1.
# Aug 25, 2019
# 2.
# Nov 23, 2019

# Say you have an array for which the i-th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
# Example 1:
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4),
# profit = 4-2 = 2.
# Example 2:
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
# profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3),
#              profit = 3-0 = 3.


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0

        ret = 0
        if k >= len(prices) / 2:
            for i in range(1, len(prices)):
                ret += max(0, prices[i] - prices[i - 1])
            return ret

        dp = [float('-inf')] * 2 * k

        for p in prices:
            for i in range(k):
                if i != 0:
                    dp[2*i] = max(dp[2*i], dp[2*i-1] - p)
                else:
                    dp[2*i] = max(dp[2*i], - p)

                dp[2*i + 1] = max(dp[2*i + 1], dp[2*i] + p)

        return dp[-1]
