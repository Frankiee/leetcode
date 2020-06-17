# https://leetcode.com/problems/android-unlock-patterns/
# 351. Android Unlock Patterns

# History:
# TikTok
# 1.
# May 27, 2020

# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the
# total number of unlock patterns of the Android lock screen, which consist of minimum of m keys
# and maximum n keys.
#
#
#
# Rules for a valid pattern:
#
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys,
# the other keys must have previously selected in the pattern. No jumps through non selected key
# is allowed.
# The order of keys used matters.
#
#
#
#
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
#
#
# Example:
#
# Input: m = 1, n = 1
# Output: 9


class Solution(object):
    SKIP = {
        (1, 7): 4,
        (1, 3): 2,
        (1, 9): 5,
        (2, 8): 5,
        (3, 7): 5,
        (3, 9): 6,
        (4, 6): 5,
        (7, 9): 8,
    }

    def _dfs(self, curr, last, m, n):
        if len(curr) >= m:
            self.ret += 1
        if len(curr) == n:
            return

        for d in range(1, 10):
            if d not in curr:
                small, big = min(last, d), max(last, d)
                if (small, big) not in self.SKIP or self.SKIP[(small, big)] in curr:
                    self._dfs(curr + [d], d, m, n)

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.ret = 0

        for d in range(1, 10):
            self._dfs([d], d, m, n)

        return self.ret
