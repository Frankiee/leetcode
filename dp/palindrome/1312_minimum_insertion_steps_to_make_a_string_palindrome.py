# [Classic, Palindrome]
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# 1312. Minimum Insertion Steps to Make a String Palindrome

# History:
# Google
# 1.
# Aug 2, 2020

# Given a string s. In one step you can insert any character at any index of the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as forward.
#
#
#
# Example 1:
#
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any insertions.
# Example 2:
#
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:
#
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# Example 4:
#
# Input: s = "g"
# Output: 0
# Example 5:
#
# Input: s = "no"
# Output: 1
#
#
# Constraints:
#
# 1 <= s.length <= 500
# All characters of s are lower case English letters.


class Solution(object):
    def __init__(self):
        self.mem = {}

    def _min_insertions(self, s, l, r):
        if l >= r:
            return 0

        if (l, r) in self.mem:
            return self.mem[(l, r)]

        if s[l] == s[r]:
            ret = self._min_insertions(s, l + 1, r - 1)
            self.mem[(l, r)] = ret

            return ret
        else:
            ret = 1 + min(
                self._min_insertions(s, l, r - 1),
                self._min_insertions(s, l + 1, r),
            )
            self.mem[(l, r)] = ret

            return ret

    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self._min_insertions(s, 0, len(s) - 1)
