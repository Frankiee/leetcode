# [Classic, 2-Pointers-Sliding-Window]
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# 395. Longest Substring with At Least K Repeating Characters

# History:
# Facebook
# 1.
# May 5, 2020

# Find the length of the longest substring T of a given string (consists of lowercase letters
# only) such that every character in T appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


class SolutionRecursion(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max([self.longestSubstring(t, k) for t in s.split(c)])

        return len(s)


from collections import defaultdict


class SolutionSlidingWindow(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret = 0
        for max_unique_chars in range(1, 27):
            counter = defaultdict(int)
            unique_chars = 0
            unique_chars_ge_k = 0

            l = 0
            for r in range(len(s)):
                counter[s[r]] += 1
                if counter[s[r]] == 1:
                    unique_chars += 1
                if counter[s[r]] == k:
                    unique_chars_ge_k += 1

                while unique_chars > max_unique_chars:
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        unique_chars -= 1
                    if counter[s[l]] == k - 1:
                        unique_chars_ge_k -= 1
                    l += 1

                if unique_chars_ge_k == unique_chars:
                    ret = max(ret, r - l + 1)

        return ret
