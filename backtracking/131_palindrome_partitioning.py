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

    def dfs(self, s, start, ret, temp):
        for i in range(start + 1, len(s) + 1):
            if self.is_palindrome(s[start:i]):
                new_temp = temp[:]
                new_temp.append(s[start:i])
                if i == len(s):
                    ret.append(new_temp)
                else:
                    self.dfs(s, i, ret, new_temp)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        ret = []
        self.dfs(s, 0, ret, [])
        return ret
