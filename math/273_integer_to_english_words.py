# [Classic]
# https://leetcode.com/problems/integer-to-english-words/
# 273. Integer to English Words

# History:
# Facebook
# 1.
# Mar 22, 2020
# 2.
# Apr 3, 2020
# 3.
# May 6, 2020

# Convert a non-negative integer to its english words representation. Given input is guaranteed
# to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight
# Hundred Ninety One"


class Solution(object):
    TO_19 = [
        'One',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten',
        'Eleven',
        'Twelve',
        'Thirteen',
        'Fourteen',
        'Fifteen',
        'Sixteen',
        'Seventeen',
        'Eighteen',
        'Nineteen',
    ]
    TENS = [
        'Twenty',
        'Thirty',
        'Forty',
        'Fifty',
        'Sixty',
        'Seventy',
        'Eighty',
        'Ninety',
    ]

    def _words(self, num):
        if num == 0:
            return []
        if num < 20:
            return [self.TO_19[num-1]]
        if num < 100:
            return [self.TENS[num / 10 - 2]] + self._words(num % 10)
        if num < 1000:
            return self._words(num / 100) + ['Hundred'] + self._words(num % 100)
        if num < 1000000:
            return self._words(num / 1000) + ['Thousand'] + self._words(num % 1000)
        if num < 1000000000:
            return self._words(num / 1000000) + ['Million'] + self._words(num % 1000000)
        if num < 1000000000000:
            return self._words(num / 1000000000) + ['Billion'] + self._words(num % 1000000000)
        # if num < 1000000000000000:
        #     return self._words(num / 1000000000000) + ['Trillion'] + self._words(num % 1000000000000)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return " ".join(self._words(num)) or 'Zero'