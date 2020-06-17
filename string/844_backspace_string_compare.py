# [Classic]
# https://leetcode.com/problems/backspace-string-compare/
# 844. Backspace String Compare

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# Apr 8, 2020
# 3.
# May 12, 2020

# Given two strings S and T, return if they are equal when both are typed into empty text
# editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?


class Solution(object):
    def _get_preceeding_idx(self, txt, i):
        hash_char_diff = 0
        while i >= 0 and (txt[i] == '#' or hash_char_diff > 0):
            if txt[i] == '#':
                hash_char_diff += 1
            else:
                hash_char_diff -= 1
            i -= 1

        return i

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if not S or not T:
            return S == T

        s_i, t_i = len(S) - 1, len(T) - 1

        while True:
            s_i = self._get_preceeding_idx(S, s_i)
            t_i = self._get_preceeding_idx(T, t_i)

            if s_i == -1 or t_i == -1:
                return s_i == t_i

            if S[s_i] != T[t_i]:
                return False

            s_i -= 1
            t_i -= 1
