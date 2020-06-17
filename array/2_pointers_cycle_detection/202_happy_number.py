# [2-Pointers-Cycle-Detection]
# https://leetcode.com/problems/happy-number/
# 202. Happy Number

# History:
# Apple
# 1.
# Mar 21, 2020

# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive
# integer, replace the number by the sum of the squares of its digits, and repeat the process
# until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
# include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    def _next_iter(self, n):
        ret = 0

        while n:
            nxt_digit = n % 10
            ret += nxt_digit ** 2
            n /= 10

        return ret

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n

        while fast != 1:
            slow = self._next_iter(slow)
            fast = self._next_iter(fast)
            fast = self._next_iter(fast)

            if fast != 1 and slow == fast:
                return False

        return True
