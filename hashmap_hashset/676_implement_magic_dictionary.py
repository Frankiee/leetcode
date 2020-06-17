# [Classic]
# https://leetcode.com/problems/implement-magic-dictionary/
# 676. Implement Magic Dictionary

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# May 4, 2020

# Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one
# character into another character in this word, the modified word is in the dictionary you just
# built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly
# efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary,
# as static/class variables are persisted across multiple test cases. Please see here for more
# details.


from collections import defaultdict


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.star_words = defaultdict(int)
        self.original_words = set()

    def _get_star_words(self, word):
        ret = set()
        for i in range(len(word)):
            ret.add(word[:i] + '*' + word[i + 1:])

        return ret

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            for star_word in self._get_star_words(word):
                self.star_words[star_word] += 1

            self.original_words.add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying
        exactly one character
        :type word: str
        :rtype: bool
        """
        star_words = self._get_star_words(word)

        if word in self.original_words:
            return any([self.star_words[s] > 1 for s in star_words])

        return any([self.star_words[s] >= 1 for s in star_words])

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
