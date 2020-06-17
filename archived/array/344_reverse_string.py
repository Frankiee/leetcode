# [Archived]
# https://leetcode.com/problems/reverse-string/
# 344. Reverse String

# History:
# Facebook
# 1.
# Feb 22, 2020
# 2.
# Apr 28, 2020

# Write a function that reverses a string. The input string is given as an array of characters
# char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return s

        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1
