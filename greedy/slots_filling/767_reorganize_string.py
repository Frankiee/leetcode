# [Greedy, Slots-Filling]
# https://leetcode.com/problems/reorganize-string/
# 767. Reorganize String

# History:
# Facebook
# 1.
# Dec 16, 2019
# 2.
# Apr 30, 2020

# Given a string S, check if the letters can be rearranged so that two characters that are
# adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"416
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].


from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = Counter(S)

        max_freq = 0
        max_freq_char = None

        for c, f in counter.iteritems():
            if f > max_freq:
                max_freq = f
                max_freq_char = c

        remaining_char_freq = len(S) - max_freq

        if remaining_char_freq < max_freq - 1:
            return ""

        ret = [[max_freq_char] for _ in range(max_freq)]

        ret_idx = 0
        for c, f in counter.iteritems():
            if c == max_freq_char:
                continue

            for i in range(f):
                ret[ret_idx % max_freq].append(c)
                ret_idx += 1

        return "".join(["".join(bucket) for bucket in ret])
