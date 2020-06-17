# [Classic]
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
# 1269. Number of Ways to Stay in the Same Place After Some Steps

# History:
# Facebook
# 1.
# Mar 1, 2020
# 2.
# May 11, 2020

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position
# to the left, 1 position to the right in the array or stay in the same place  (The pointer
# should not be placed outside the array at any time).
#
# Given two integers steps and arrLen, return the number of ways such that your pointer still at
# index 0 after exactly steps steps.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# Example 2:
#
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# Example 3:
#
# Input: steps = 4, arrLen = 2
# Output: 8
#
#
# Constraints:
#
# 1 <= steps <= 500
# 1 <= arrLen <= 10^6

from collections import defaultdict


class SolutionDict(object):
    MOD = 10 ** 9 + 7

    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        dp = defaultdict(int)
        dp[0] = 1

        for _ in range(steps):
            nxt_dp = defaultdict(int)

            for pos, ways in dp.iteritems():
                nxt_dp[pos] += ways
                if pos + 1 < arrLen:
                    nxt_dp[pos + 1] += ways
                if pos - 1 >= 0:
                    nxt_dp[pos - 1] += ways

            dp = nxt_dp

        return dp[0] % self.MOD


class SolutionArray(object):
    MOD = 10 ** 9 + 7

    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        length = min(arrLen, steps)
        dp = [0] * length
        dp[0] = 1

        for _ in range(steps):
            nxt_dp = dp[::]

            for i in range(length):
                if i - 1 >= 0:
                    nxt_dp[i] += dp[i - 1]
                if i + 1 < length:
                    nxt_dp[i] += dp[i + 1]

                if nxt_dp[i] == 0:
                    break

            dp = nxt_dp

        return dp[0] % self.MOD


class Solution2(object):
    MOD = 10 ** 9 + 7

    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        if steps == 0:
            return 1

        arrLen = min(arrLen, steps + 1)
        ways_a = [0] * arrLen
        ways_b = [0] * arrLen
        current_ways = ways_a

        for s in range(steps):
            nxt_ways = ways_a if current_ways == ways_b else ways_b
            if s == 0:
                nxt_ways[0] = 1
                nxt_ways[1] = 1
            else:
                for i in range(min(arrLen, s + 2)):
                    nxt_ways[i] = current_ways[i]
                    if i > 0:
                        nxt_ways[i] += current_ways[i - 1]
                    if i < arrLen - 1:
                        nxt_ways[i] += current_ways[i + 1]
                    nxt_ways[i] %= self.MOD

            current_ways = nxt_ways

        return nxt_ways[0]
