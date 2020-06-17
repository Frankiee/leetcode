# [Classic]
# https://leetcode.com/problems/handshakes-that-dont-cross/
# 1259. Handshakes That Don't Cross

# History:
# Facebook, TikTok
# 1.
# Apr 26, 2020

# You are given an even number of people num_people that stand around a circle and each person
# shakes hands with someone else, so that there are num_people / 2 handshakes total.
#
# Return the number of ways these handshakes could occur such that none of the handshakes cross.
#
# Since this number could be very big, return the answer mod 10^9 + 7
#
#
#
# Example 1:
#
# Input: num_people = 2
# Output: 1
# Example 2:
#
#
#
# Input: num_people = 4
# Output: 2
# Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is
# [(2,3),(4,1)].
# Example 3:
#
#
#
# Input: num_people = 6
# Output: 5
# Example 4:
#
# Input: num_people = 8
# Output: 14
#
#
# Constraints:
#
# 2 <= num_people <= 1000
# num_people % 2 == 0


class Solution(object):
    MOD = 10 ** 9 + 7

    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        if num_people == 0:
            return 0
        if num_people == 2:
            return 1

        dp = [None] * (num_people / 2 + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, num_people / 2 + 1):
            ret = 0
            for l in range(i):
                ret += dp[l] * (dp[i - l - 1])

            dp[i] = ret % self.MOD

        return dp[-1]
