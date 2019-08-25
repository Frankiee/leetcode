# [Archived]
# https://leetcode.com/problems/ransom-note/
# 383. Ransom Note

# Given an arbitrary ransom note string and another string containing
# letters from all the magazines, write a function that will return true if
# the ransom note can be constructed from the magazines ; otherwise, it will
# return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True

        if len(ransomNote) > len(magazine):
            return False

        ransom_note_counter = Counter(list(ransomNote))
        magazine_counter = Counter(list(magazine))

        return all([
            char in magazine_counter and ct <= magazine_counter[char]
            for char, ct in ransom_note_counter.iteritems()
        ])
