# https://leetcode.com/problems/largest-multiple-of-three/
# 1363. Largest Multiple of Three

# History:
# ByteDance
# 1.
# Mar 26, 2020

# Given an integer array of digits, return the largest multiple of three that can be formed by
# concatenating some of the given digits in any order.
#
# Since the answer may not fit in an integer data type, return the answer as a string.
#
# If there is no answer return an empty string.
#
#
#
# Example 1:
#
# Input: digits = [8,1,9]
# Output: "981"
# Example 2:
#
# Input: digits = [8,6,7,1,0]
# Output: "8760"
# Example 3:
#
# Input: digits = [1]
# Output: ""
# Example 4:
#
# Input: digits = [0,0,0,0,0,0]
# Output: "0"
#
#
# Constraints:
#
# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9
# The returning answer must not contain unnecessary leading zeros.


from collections import Counter


class Solution(object):
    def _pop_and_ret(self, counter, digit):
        if counter[digit] != 0:
            counter[digit] -= 1

        total = sum([d * f for d, f in counter.iteritems()])
        if total % 3 == 0:
            ret = ""
            for d in range(9, -1, -1):
                ret += str(d) * counter[d]
            return ret if not ret else str(int(ret))

    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        total = sum(digits)
        counter = Counter(digits)

        if total % 3 == 0:
            return self._pop_and_ret(counter, None)
        elif total % 3 == 1 and (counter[1] or counter[4] or counter[7]):
            return (
                self._pop_and_ret(counter, 1) or
                self._pop_and_ret(counter, 4) or
                self._pop_and_ret(counter, 7)
            )
        elif total % 3 == 2 and (counter[2] or counter[5] or counter[8]):
            return (
                self._pop_and_ret(counter, 2) or
                self._pop_and_ret(counter, 5) or
                self._pop_and_ret(counter, 8)
            )
        elif total % 3 == 2:
            return (
                self._pop_and_ret(counter, 1) or
                self._pop_and_ret(counter, 1) or
                self._pop_and_ret(counter, 4) or
                self._pop_and_ret(counter, 4) or
                self._pop_and_ret(counter, 7) or
                self._pop_and_ret(counter, 7)
            )

        return (
            self._pop_and_ret(counter, 2) or
            self._pop_and_ret(counter, 2) or
            self._pop_and_ret(counter, 5) or
            self._pop_and_ret(counter, 5) or
            self._pop_and_ret(counter, 8) or
            self._pop_and_ret(counter, 8)
        )
