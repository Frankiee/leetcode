# [Count-Number-Up-To-N, Classic]
# https://leetcode.com/problems/rotated-digits/
# 788. Rotated Digits

# History:
# Google, Facebook
# 1.
# Mar 26, 2020
# 2.
# May 12, 2020

# X is a good number if after rotating each digit individually by 180 degrees, we get a valid
# number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to
# themselves; 2 and 5 rotate to each other (on this case they are rotated in a different
# direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of
# the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].


class Solution1(object):
    HAPPY_DIGITS = {1, 8, 0}
    ROTATABLE_DIGITS = {1, 8, 0, 6, 9, 2, 5}

    def _is_happy_number(self, n):
        digits = set([int(i) for i in str(n)])

        return digits.issubset(self.ROTATABLE_DIGITS) and not digits.issubset(self.HAPPY_DIGITS)

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return sum([self._is_happy_number(i) for i in range(1, N + 1)])


class Solution2(object):
    ROTATABLE_DIFF_DIGITS = {2, 5, 6, 9}
    ROTATABLE_DIGITS = {0, 1, 8, 2, 5, 6, 9}

    def _is_good_numer(self, n):
        digits = [int(d) for d in str(n)]

        return (all([d in self.ROTATABLE_DIGITS for d in digits]) and
                any([d in self.ROTATABLE_DIFF_DIGITS for d in digits]))

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return sum([1 for i in range(N + 1) if self._is_good_numer(i)])
