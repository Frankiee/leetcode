# [Classic, Backtracking]
# https://leetcode.com/problems/optimal-account-balancing/
# 465. Optimal Account Balancing

# History:
# TikTok
# 1.
# Apr 26, 2020

# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid
# for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each
# transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill,
# and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions
# can be represented as [[0, 1, 10], [2, 0, 5]].
#
# Given a list of transactions between a group of people, return the minimum number of
# transactions required to settle the debt.
#
# Note:
#
# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have
# the persons 0, 2, 6.
# Example 1:
#
# Input:
# [[0,1,10], [2,0,5]]
#
# Output:
# 2
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
#
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5
# each.
# Example 2:
#
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#
# Output:
# 1
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
#
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.


from collections import defaultdict


class Solution(object):
    def _dfs(self, start_idx, debt):
        if start_idx == len(debt):
            return 0

        if debt[start_idx] == 0:
            return self._dfs(start_idx + 1, debt)

        ret = float('inf')
        for to_swap in range(start_idx + 1, len(debt)):
            if debt[to_swap] * debt[start_idx] < 0:
                debt[to_swap] += debt[start_idx]
                ret = min(ret, 1 + self._dfs(start_idx + 1, debt))
                debt[to_swap] -= debt[start_idx]

        return ret

    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        debt = defaultdict(int)

        for p1, p2, amount in transactions:
            debt[p1] += amount
            debt[p2] -= amount

        debt = debt.values()

        return self._dfs(0, debt)
