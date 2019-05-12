# https://leetcode.com/problems/valid-palindrome-ii/
# 680. Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge
# whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length
# of the string is 50000.


class Solution(object):
    def valid_palindrome(self, s, drop_char):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if drop_char:
                    return (
                        self.valid_palindrome(s[l:r], False) or
                        self.valid_palindrome(s[l + 1:r + 1], False)
                    )
                else:
                    return False

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [c.lower() for c in s if c.isalnum()]

        return self.valid_palindrome(s, True)
