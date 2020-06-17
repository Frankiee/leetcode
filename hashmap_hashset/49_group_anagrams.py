# [Hash]
# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams

# History:
# Facebook
# 1.
# Dec 14, 2019
# 2.
# May 3, 2020

# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict


class Solution(object):
    BASE = ord('a')

    def _get_root(self, word):
        root = [0] * 26

        for c in word:
            root[ord(c) - self.BASE] += 1

        return tuple(root)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = defaultdict(list)

        for s in strs:
            mp[self._get_root(s)].append(s)

        return mp.values()
