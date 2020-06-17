# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/grumpy-bookstore-owner/
# 1052. Grumpy Bookstore Owner

# History:
# 1.
# Sep 14, 2019
# 2.
# Nov 13, 2019

# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store,
# and all those customers leave after the end of that minute.
#
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When
# the bookstore owner is grumpy, the customers of that minute are not
# satisfied, otherwise they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy
# for X minutes straight, but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout
# the day.
#
#
# Example 1:
#
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last
# 3 minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7
# + 5 = 16.
#
#
# Note:
#
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        satisfied_without_technique = sum([
            c
            for c, g in zip(customers, grumpy)
            if g == 0
        ])

        add_satisfied_with_technique = 0
        max_add_satisfied_with_technique = 0
        for i in range(X):
            if grumpy[i] == 1:
                add_satisfied_with_technique += customers[i]
        max_add_satisfied_with_technique = add_satisfied_with_technique

        for i in range(X, len(customers)):
            if grumpy[i] == 1:
                add_satisfied_with_technique += customers[i]
            if grumpy[i - X] == 1:
                add_satisfied_with_technique -= customers[i - X]

            max_add_satisfied_with_technique = max(
                max_add_satisfied_with_technique,
                add_satisfied_with_technique,
            )

        return satisfied_without_technique + max_add_satisfied_with_technique
