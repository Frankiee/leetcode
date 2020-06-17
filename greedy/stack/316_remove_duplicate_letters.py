# [Greedy, Classic, Stack]
# https://leetcode.com/problems/remove-duplicate-letters/
# 316. Remove Duplicate Letters

# History:
# 1.
# Aug 25, 2019
# 2.
# Dec 1, 2019

# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make
# sure your result is the smallest in lexicographical order among all
# possible results.
#
# Example 1:
#
# Input: "bcabc"
# Output: "abc"
# Example 2:
#
# Input: "cbacdcbc"
# Output: "acdb"

from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        coutner = Counter(s)
        used = set()

        for c in s:
            coutner[c] -= 1

            if c in used:
                continue

            while stack and ord(stack[-1]) > ord(c) and coutner[stack[-1]] > 0:
                used.remove(stack[-1])
                stack.pop(-1)

            used.add(c)
            stack.append(c)

        return "".join(stack)
