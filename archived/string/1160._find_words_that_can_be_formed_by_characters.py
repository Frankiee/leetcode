# [Archived]
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# 1160. Find Words That Can Be Formed by Characters

# History:
# 1.
# Sep 19, 2021

# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

from collections import Counter


class Solution(object):
    def _is_subset(self, w, chars_counter):
        w_counter = Counter(w)

        for c, ct in w_counter.items():
            if chars_counter[c] < ct:
                return False

        return True

    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_counter = Counter(chars)

        ret = 0
        for w in words:
            if self._is_subset(w, chars_counter):
                ret += len(w)

        return ret
