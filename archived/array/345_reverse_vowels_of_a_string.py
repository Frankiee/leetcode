# [Archived]
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# 345. Reverse Vowels of a String

# Write a function that takes a string as input and reverse only the vowels
# of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] not in self.VOWELS:
                l += 1
                continue

            if s[r] not in self.VOWELS:
                r -= 1
                continue

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
