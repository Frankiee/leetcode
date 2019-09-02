# [Prime-Factor, Ugly-Number]
# https://leetcode.com/problems/super-ugly-number/
# 313. Super Ugly Number

# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
#
# Example:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12
#              super ugly numbers given primes = [2,7,13,19] of size 4.
# Note:
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1]
        prime_num_idx = [0] * len(primes)

        while n > 1:
            next_num_candidates = [
                primes[idx] * dp[prime_num_idx[idx]]
                for idx in range(len(primes))
            ]

            next_num = min(next_num_candidates)

            for idx in range(len(primes)):
                if next_num_candidates[idx] == next_num:
                    prime_num_idx[idx] += 1

            dp.append(next_num)
            n -= 1

        return dp[-1]
