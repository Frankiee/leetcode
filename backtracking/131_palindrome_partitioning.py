# https://leetcode.com/problems/palindrome-partitioning/description/
# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition
# is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def is_palindrome(self, s):
        return s == s[::-1]

    def dfs(self, ret, s, start, prefix):
        if start == len(s):
            ret.append(prefix)
        else:
            for i in range(start + 1, len(s) + 1):
                new_word = s[start:i]
                if self.is_palindrome(new_word):
                    self.dfs(ret, s, i, prefix + [new_word])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []

        self.dfs(ret, s, 0, [])

        return ret
