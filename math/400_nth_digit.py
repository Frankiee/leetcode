# https://leetcode.com/problems/nth-digit/
# 400. Nth Digit

# History:
# Facebook
# 1.
# May 12, 2020

# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of
# the number 10.


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        digit, count, num = 1, 9, 0

        while True:
            if digit * count > n:
                num_idx = n / digit
                return str(num_idx + num + 1)[n % digit]

            n -= digit * count
            num += count
            digit = digit + 1
            count = count * 10
