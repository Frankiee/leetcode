# [Important]
# https://leetcode.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = set()
        non_repeating_chars = OrderedDict()

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in mem:
                mem.add(s[i])
                non_repeating_chars[s[i]] = i
            else:
                if s[i] in non_repeating_chars:
                    del non_repeating_chars[s[i]]

        return non_repeating_chars.popitem(last=True)[
            1] if non_repeating_chars else -1
