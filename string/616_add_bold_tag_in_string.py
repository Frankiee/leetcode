# [Classic, Boolean-Array]
# https://leetcode.com/problems/add-bold-tag-in-string/
# 616. Add Bold Tag in String

# History:
# Facebook
# 1.
# Mar 1, 2020
# 2.
# Apr 30, 2020

# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and
# </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need
# to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by
# bold tags are consecutive, you need to combine them.
# Example 1:
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].


class Solution(object):
    TAG_OPEN = "<b>"
    TAG_CLOSE = "</b>"

    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        status = [False] * len(s)

        for word in dict:
            next_start = 0
            length = len(word)

            while next_start != -1:
                next_start = s.find(word, next_start)

                if next_start != -1:
                    for i in range(next_start, next_start + length):
                        status[i] = True

                    next_start += 1

        curr_tag = False
        ret = []
        for i in range(len(s)):
            if status[i] and not curr_tag:
                curr_tag = True
                ret.append(self.TAG_OPEN)
            elif not status[i] and curr_tag:
                curr_tag = False
                ret.append(self.TAG_CLOSE)

            ret.append(s[i])

        if status[-1]:
            ret.append(self.TAG_CLOSE)

        return "".join(ret)
