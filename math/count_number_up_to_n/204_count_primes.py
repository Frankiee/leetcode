# [Count-Number-Up-To-N, Prime-Factor, Classic]
# https://leetcode.com/problems/count-primes/
# 204. Count Primes

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://www.youtube.com/watch?v=Kwo2jkHOyPY

# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [True] * n

        for i in range(2, int(n ** 0.5 + 1)):
            if dp[i]:
                # set times of i to False starting from i^2
                for time in range(i * i, n, i):
                    dp[time] = False

        return len([1 for i in range(2, n) if dp[i] == True])


# Appendix: is_prime implementation
def is_prime(n):
    for i in range(2, int(n ** 0.5 + 2)):
        if i < n and n % i == 0:
            return False

    return True
