# https://leetcode.com/problems/word-pattern/
# 290. Word Pattern

# History:
# 1.
# Mar 17, 2020

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and
# a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that
# may be separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_split = str.split(' ')

        if len(str_split) != len(pattern):
            return False

        forward_mp = {}
        str_seen = set()
        for i in range(len(pattern)):
            if pattern[i] not in forward_mp:
                if str_split[i] in str_seen:
                    return False
                forward_mp[pattern[i]] = str_split[i]
                str_seen.add(str_split[i])
            else:
                if forward_mp[pattern[i]] != str_split[i]:
                    return False

        return True
