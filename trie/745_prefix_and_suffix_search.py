# https://leetcode.com/problems/prefix-and-suffix-search/
# 745. Prefix and Suffix Search

# Given many words, words[i] has weight i.
#
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix). It will return the word with given prefix and
# suffix with maximum weight. If no word exists, return -1.
#
# Examples:
#
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
#
#
# Note:
#
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.


class TrieNode(object):
    def __init__(self, max_index=None):
        self.max_index = max_index
        self.is_word = False
        self.children = {}


class PrefixSuffixTrie(object):
    def __init__(self):
        self.trie = TrieNode()

    def _insert(self, word, index):
        node = self.trie

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
            node.max_index = index

        node.is_word = True

    def insert_combo(self, word, index):
        for i in range(len(word) + 1):
            w = word[i:] + '_' + word
            self._insert(w, index)

    def search(self, word):
        node = self.trie

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return -1

        return node.max_index


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = PrefixSuffixTrie()

        for idx, w in enumerate(words):
            self.trie.insert_combo(w, idx)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.trie.search(suffix + '_' + prefix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
