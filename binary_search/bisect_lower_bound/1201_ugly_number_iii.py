# [Bisect-Lower-Bound]
# https://leetcode.com/problems/ugly-number-iii/
# 1201. Ugly Number III

# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive integers which are divisible by a or b or c.
#
#
#
# Example 1:
#
# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# Example 2:
#
# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# Example 3:
#
# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is
# 10.
# Example 4:
#
# Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
# Output: 1999999984
#
#
# Constraints:
#
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# It's guaranteed that the result will be in range [1, 2 * 10^9]


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        l = 1
        r = sys.maxsize

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)

        while l < r:
            m = l + (r - l) / 2

            m_idx = (
                m / a + m / b + m / c + m / abc
                - m / ab - m / ac - m / bc
            )

            if m_idx >= n:
                r = m
            else:
                l = m + 1

        return l
