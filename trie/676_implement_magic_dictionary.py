# [Important]
# https://leetcode.com/problems/implement-magic-dictionary/
# 676. Implement Magic Dictionary

# Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words
# to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word,
# the modified word is in the dictionary you just built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple
# test cases. Please see here for more details.


class TrieNode(object):
    def __init__(self):
        self.asterisk_chars = {}
        self.children = {}
        self.is_word = False


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fuzzy_trie = TrieNode()

    def _generate_asterisk_words(self, word):
        ret = []

        for i in range(len(word)):
            asterisk_char = word[i]
            new_word = word[:i] + '*' + word[i + 1:]
            ret.append((new_word, asterisk_char))

        return ret

    def _add_word_to_trie(self, word, asterisk_char):
        current_trie_node = self.fuzzy_trie
        for c in word:
            if c in current_trie_node.children:
                current_trie_node = current_trie_node.children[c]
            else:
                new_node = TrieNode()
                current_trie_node.children[c] = new_node
                current_trie_node = new_node

        if word in current_trie_node.asterisk_chars:
            current_trie_node.asterisk_chars[word].add(asterisk_char)
        else:
            current_trie_node.asterisk_chars[word] = {asterisk_char}
        current_trie_node.is_word = True

    def buildDict(self, dict_words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict_words:
            asterisk_words = self._generate_asterisk_words(word)

            for asterisk_word, asterisk_char in asterisk_words:
                self._add_word_to_trie(asterisk_word, asterisk_char)

    def search_asterisk_word(self, word, exclusive_char):
        current_trie_node = self.fuzzy_trie
        for c in word:
            if c not in current_trie_node.children:
                return False

            current_trie_node = current_trie_node.children[c]

        if not current_trie_node.is_word:
            return False
        if current_trie_node.asterisk_chars[word] == {exclusive_char}:
            return False

        return True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given
        word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        asterisk_words = self._generate_asterisk_words(word)

        for word, exclusive_char in asterisk_words:
            if self.search_asterisk_word(word, exclusive_char):
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
