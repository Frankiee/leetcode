# [Knuth–Morris–Pratt]
# https://leetcode.com/problems/implement-strstr/
# 28. Implement strStr()

# History:
# Facebook
# 1.
# May 18, 2019
# 2.
# Mar 27, 2020

# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().


class Solution(object):
    def _build_lps(self, needle):
        longest_prefix_surfix = [0] * len(needle)

        current_longest = 0
        needle_idx = 1
        while needle_idx < len(needle):
            if needle[needle_idx] == needle[current_longest]:
                current_longest += 1
                longest_prefix_surfix[needle_idx] = current_longest
                needle_idx += 1
            else:
                if current_longest == 0:
                    current_longest = longest_prefix_surfix[
                        current_longest - 1]
                    longest_prefix_surfix[needle_idx] = current_longest
                    needle_idx += 1
                else:
                    current_longest = longest_prefix_surfix[
                        current_longest - 1]

        return longest_prefix_surfix

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        longest_prefix_surfix = self._build_lps(needle)

        current_needle_idx = 0
        haystack_idx = 0
        while haystack_idx < len(haystack):
            if haystack[haystack_idx] == needle[current_needle_idx]:
                if current_needle_idx == len(needle) - 1:
                    return haystack_idx - len(needle) + 1

                current_needle_idx += 1
                haystack_idx += 1
            else:
                if current_needle_idx == 0:
                    haystack_idx += 1
                else:
                    current_needle_idx = longest_prefix_surfix[
                        current_needle_idx - 1]

        return -1


class SolutionStringComparison(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i

        return -1
