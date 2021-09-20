# [Classic]
# https://leetcode.com/problems/longest-common-prefix/submissions/
# 14. Longest Common Prefix

# History:
# Apple
# 1.
# May 8, 2020
# 2.
# Sep 18, 2021

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_i = 0
        while True:
            for i, s in enumerate(strs):
                if i == 0:
                    if longest_i >= len(s):
                        return s[:longest_i]
                else:
                    if longest_i >= len(s) or s[longest_i] != strs[i-1][longest_i]:
                        return s[:longest_i]
            longest_i += 1


class SolutionShortestStr(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s

        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]

        return shortest


class SolutionZip(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        for i, lst in enumerate(zip(*strs)):
            if len(set(lst)) != 1:
                break
            ret += lst[0]

        return ret



from collections import defaultdict


class SolutionCounter(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        mp = defaultdict(int)

        longest_so_far = min([len(s) for s in strs])
        for i, s in enumerate(strs):
            for j in range(min(len(s), longest_so_far)):
                c = s[j]
                hs = str(j) + c
                mp[hs] += 1

                if mp[hs] != i + 1:
                    longest_so_far = j
                    break
                else:
                    longest_so_far = j + 1

        return strs[0][:longest_so_far]
