# [Archived]
# https://leetcode.com/problems/number-of-different-integers-in-a-string/
# 1805. Number of Different Integers in a String

# History:
# 1.
# Apr 10, 2021

# You are given a string word that consists of digits and lowercase English letters.
#
# You will replace every non-digit character with a space.
# For example, "a123bc34d8ef34" will become " 123  34 8  34".
# Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
#
# Return the number of different integers after performing the replacement operations on word.
#
# Two integers are considered different if their decimal representations without any leading zeros are different.
#
#
#
# Example 1:
#
# Input: word = "a123bc34d8ef34"
# Output: 3
# Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
# Example 2:
#
# Input: word = "leet1234code234"
# Output: 2
# Example 3:
#
# Input: word = "a1b01c001"
# Output: 1
# Explanation: The three integers "1", "01", and "001" all represent the same integer because
# the leading zeros are ignored when comparing their decimal values.
#
#
# Constraints:
#
# 1 <= word.length <= 1000
# word consists of digits and lowercase English letters.

class Solution(object):
    def _isdigit(self, c):
        return '0' <= c <= '9'

    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        ret = set()
        digit_start = None
        for i in range(len(word) + 1):
            if i < len(word) and self._isdigit(word[i]):
                if digit_start is None:
                    digit_start = i
            else:
                if i > 0 and self._isdigit(word[i - 1]):
                    ret.add(int(word[digit_start:i]))
                digit_start = None

        return len(ret)
