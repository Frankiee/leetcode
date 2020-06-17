# https://leetcode.com/problems/verifying-an-alien-dictionary/
# 953. Verifying an Alien Dictionary

# History:
# Facebook
# 1.
# Jan 29, 2020
# 2.
# Apr 1, 2020
# 3.
# Apr 24, 2020

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a
# different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the
# sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in
# size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is
# defined as the blank character which is less than any other character (More info).
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.


class Solution(object):
    def _verify(self, w1, w2, position):
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                return position[w1[i]] < position[w2[i]]

        return len(w1) < len(w2)

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        position = {}
        for i, c in enumerate(order):
            position[c] = i

        for i in range(len(words) - 1):
            if not self._verify(words[i], words[i + 1], position):
                return False

        return True
