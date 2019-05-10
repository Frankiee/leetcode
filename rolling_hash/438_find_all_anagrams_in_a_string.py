# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 438. Find All Anagrams in a String

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
