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
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        l = 0
        r = len(s) - 1
        s = list(s)

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)
