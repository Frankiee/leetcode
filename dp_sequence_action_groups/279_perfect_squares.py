# https://leetcode.com/problems/perfect-squares/
# 279. Perfect Squares

# Given a positive integer n, find the least number of perfect square
# numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution(object):
    def _is_square(self, n):
        return n ** 0.5 == int(n ** 0.5)

    def numSquares(self, n):
        """
        :type c: int
        :rtype: list
        """
        dp = [float('-inf')] * (n + 1)

        for i in range(1, n + 1):
            if self._is_square(i):
                dp[i] = 1
            else:
                min_idx = None
                for j in range(1, int(i ** 0.5) + 1):
                    current_idx = i - j ** 2
                    if min_idx is None or dp[current_idx] < dp[min_idx]:
                        min_idx = current_idx
                dp[i] = dp[min_idx] + 1

        return dp[n]
