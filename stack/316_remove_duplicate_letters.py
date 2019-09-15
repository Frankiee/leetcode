# [Classic]
# https://leetcode.com/problems/remove-duplicate-letters/
# 316. Remove Duplicate Letters

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
        if not s:
            return ""

        counter = Counter(list(s))
        used = {}

        stack = []

        for c in s:
            counter[c] -= 1
            if c in used and used[c]:
                continue
            elif not stack:
                stack.append(c)
                used[c] = True
            else:
                while stack and c < stack[-1] and counter[stack[-1]] > 0:
                    used[stack[-1]] = False
                    stack.pop()
                stack.append(c)
                used[c] = True

        return "".join(stack)
