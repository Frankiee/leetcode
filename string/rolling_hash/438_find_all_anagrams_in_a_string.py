# [Rolling-Hash]
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 438. Find All Anagrams in a String

# History:
# Facebook
# 1.
# May 9, 2019
# 2.
# Jan 4, 2020
# 3.
# Mar 18, 2020
# 4.
# Apr 23, 2020

# Given a string s and a non-empty string p, find all the start indices of
# p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter, defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_counter = Counter(p)
        s_counter = defaultdict(int)
        char_diff = len(p)

        ret = []
        for i, c in enumerate(s):
            s_counter[c] += 1

            if c in p_counter and s_counter[c] <= p_counter[c]:
                char_diff -= 1

            if i >= len(p):
                old_c = s[i - len(p)]
                s_counter[old_c] -= 1

                if old_c in p_counter and s_counter[old_c] < p_counter[old_c]:
                    char_diff += 1

            if char_diff == 0:
                ret.append(i - len(p) + 1)

        return ret


from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        p_counter = Counter([c for c in p])

        ret = []

        for i in range(len(s) - len(p) + 1):
            if i == 0:
                s_counter = Counter([c for c in s[:len(p)]])
            else:
                s_counter[s[i - 1]] -= 1
                if s_counter[s[i - 1]] == 0:
                    del s_counter[s[i - 1]]
                s_counter[s[i + len(p) - 1]] += 1

            if p_counter == s_counter:
                ret.append(i)

        return ret
