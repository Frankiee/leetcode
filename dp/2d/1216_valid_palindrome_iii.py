# [2D-DP, Classic]
# https://leetcode.com/problems/valid-palindrome-iii/
# 1216. Valid Palindrome III

# History:
# Facebook
# 1.
# Feb 27, 2020

# Given a string s and an integer k, find out if the given string is a K-Palindrome or not.
#
# A string is K-Palindrome if it can be transformed into a palindrome by removing at most k
# characters from it.
#
#
#
# Example 1:
#
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length


class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        dp = [None] * len(s)
        for r in range(len(s)):
            dp[r] = [None] * len(s)

        for length in range(1, len(s) + 1):
            for l in range(0, len(s) - length + 1):
                r = l + length - 1

                if l == r:
                    dp[l][r] = 0
                elif s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] if length > 2 else 0
                else:
                    dp[l][r] = min(dp[l][r - 1], dp[l + 1][r]) + 1

        return dp[0][len(s) - 1] <= k
