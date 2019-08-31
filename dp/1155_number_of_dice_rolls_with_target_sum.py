# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# 1155. Number of Dice Rolls With Target Sum

# You have d dice, and each die has f faces numbered 1, 2, ..., f.
#
# Return the number of possible ways (out of fd total ways) modulo 10^9 + 7
# to roll the dice so the sum of the face up numbers equals target.
#
#
#
# Example 1:
#
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# Example 2:
#
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:
#
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation:
# You throw two dice, each with 5 faces.  There is only one way to get a sum
# of 10: 5+5.
# Example 4:
#
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation:
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# Example 5:
#
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.
#
#
# Constraints:
#
# 1 <= d, f <= 30
# 1 <= target <= 1000


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d <= 0:
            return 0

        mod = 10 ** 9 + 7
        min_num = d
        max_num = d * f

        if target > max_num or target < min_num:
            return 0

        dp1 = [0] * (target + 1)
        dp2 = [0] * (target + 1)

        pre_dp = dp1
        next_dp = dp2
        pre_dp[0] = 1
        for r in range(d):
            for i in range(r + 1, min((r + 1) * f + 1, target + 1)):
                next_dp[i] = sum([
                    pre_dp[last_i] if last_i >= 0 else 0
                    for last_i in range(i - f, i)
                ]) % mod
            next_dp[r] = 0
            if r - 1 >= 0:
                next_dp[r - 1] = 0
            pre_dp, next_dp = next_dp, pre_dp

        return pre_dp[target]
