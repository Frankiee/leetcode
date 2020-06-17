# https://leetcode.com/problems/valid-palindrome-ii/
# 680. Valid Palindrome II

# History:
# 1.
# May 12, 2019
# 2.
# Nov 12, 2019
# 3.
# Apr 23, 2020

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


class Solution1(object):
    def _is_valid_palindrome(self, s, l, r, deleted):
        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                return (
                    self._is_valid_palindrome(s, l + 1, r, True) or
                    self._is_valid_palindrome(s, l, r - 1, True)
                )

            l += 1
            r -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._is_valid_palindrome(s, 0, len(s) - 1, False)


class Solution2(object):
    def _valid_palindrome(self, s, removed, l, r):
        if l >= r:
            return True

        if s[l] == s[r]:
            return self._valid_palindrome(s, removed, l + 1, r - 1)

        if removed:
            return False

        return self._valid_palindrome(s, True, l + 1, r) or self._valid_palindrome(s, True, l,
                                                                                   r - 1)

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._valid_palindrome(s, False, 0, len(s) - 1)
