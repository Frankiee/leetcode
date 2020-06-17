# https://leetcode.com/problems/group-shifted-strings/
# 249. Group Shifted Strings

# History:
# Facebook
# 1.
# Jan 20, 2020
# 2.
# Apr 30, 2020

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc"
# -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong
# to the same shifting sequence.
#
# Example:
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

from collections import defaultdict


class Solution1(object):
    def _get_hash(self, string):
        if not string:
            return []

        ret = [0]
        for i in range(1, len(string)):
            diff = ord(string[i]) - ord(string[i - 1])
            diff = diff if diff > 0 else diff + 26
            ret.append(diff)

        return ret

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)

        for string in strings:
            dic[tuple(self._get_hash(string))].append(string)

        return dic.values()


from collections import defaultdict


class Solution2(object):
    def _get_signiture(self, string):
        if not string:
            return string

        base = ord(string[0])

        ret = []
        for c in string:
            ret.append(str((ord(c) - base) % 26))

        return ",".join(ret)

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        group = defaultdict(list)

        for string in strings:
            group[self._get_signiture(string)].append(string)

        return group.values()
