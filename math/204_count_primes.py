# [Prime-Factor, Hard]
# https://leetcode.com/problems/count-primes/
# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution(object):
    def is_prime(self, n):
        for i in range(2, int(n ** 0.5 + 2)):
            if i < n and n % i == 0:
                return False

        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [True] * n

        for i in range(2, int(n ** 0.5 + 2)):
            if self.is_prime(i):
                time = 2
                while i * time < n:
                    dp[i * time] = False
                    time += 1

        return len([1 for i in range(2, n) if dp[i] == True])
