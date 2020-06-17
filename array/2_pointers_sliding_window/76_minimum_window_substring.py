# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/minimum-window-substring/
# 76. Minimum Window Substring

# History:
# Facebook
# 1.
# Mar 15, 2020
# 2.
# Apr 22, 2020

# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return
# the empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.


from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        t_counter = Counter(t)
        matched_left = len(t)

        curr_counter = {}

        ret = None
        l = 0
        for i, c in enumerate(s):
            c_count = curr_counter[c] if c in curr_counter else 0
            t_count = t_counter[c] if c in t_counter else 0
            if c_count < t_count:
                matched_left -= 1
            curr_counter[c] = c_count + 1

            while l <= i and (s[l] not in t_counter or curr_counter[s[l]] > t_counter[s[l]]):
                curr_counter[s[l]] -= 1
                l += 1

            if matched_left == 0 and (not ret or i - l + 1 < len(ret)):
                ret = s[l:i + 1]

        return ret or ""


# Depreciated
class DepreciatedSolution(object):
    def __init__(self):
        self.s_dict = {}
        self.t_dict = {}

    def _add_item(self, dic, c):
        dic[c] = (dic.get(c) or 0) + 1

    def _remove_item(self, dic, c):
        dic[c] = dic[c] - 1
        if not dic[c]:
            del dic[c]

    def _contain_all(self):
        return all(
            t_key in self.s_dict and self.s_dict[t_key] >= t_value
            for t_key, t_value in self.t_dict.iteritems()
        )

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Initialize t_dict
        for c in t:
            self._add_item(self.t_dict, c)

        current_min_size = float('inf')
        current_min = ""

        l = 0

        for r in range(len(s)):
            self._add_item(self.s_dict, s[r])
            if self._contain_all():
                for l_iter in range(l, r + 1):
                    l = l_iter
                    if r - l + 1 < current_min_size:
                        current_min_size = r - l + 1
                        current_min = s[l:r + 1]
                    self._remove_item(self.s_dict, s[l])
                    if not self._contain_all():
                        l += 1
                        break

        return current_min
