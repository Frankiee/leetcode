# [OrderedDict]
# https://leetcode.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String

# History:
# Facebook
# 1.
# Mar 18, 2019
# 2.
# Nov 23, 2019
# 3.
# Dec 13, 2019
# 4.
# Apr 23, 2020

# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#438
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
        appeared = set()
        ordered_dict = OrderedDict()

        for i in range(len(s)):
            c = s[i]
            if c not in appeared:
                ordered_dict[c] = i
                appeared.add(c)
            elif c in ordered_dict:
                del ordered_dict[c]

        return ordered_dict.popitem(last=False)[1] if ordered_dict else -1


from collections import Counter


class SolutionCounter(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1
