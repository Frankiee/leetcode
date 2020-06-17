# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# 211. Add and Search Word - Data structure design

# History:
# Facebook
# 1.
# Jan 27, 2020
# 2.
# FB Phone Screen
# Apr 14, 2020
# 3.
# May 6, 2020

# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters
# a-z or .. A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.trie

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.is_terminal = True

    def _dfs(self, p, curr_index, curr_trie_node):
        if curr_index >= len(p):
            return curr_trie_node.is_terminal

        nxt_char = p[curr_index]

        if nxt_char.isalpha():
            if nxt_char in curr_trie_node.children:
                return self._dfs(p, curr_index + 1, curr_trie_node.children[nxt_char])
            else:
                return False
        elif nxt_char == '.':
            for n in curr_trie_node.children.values():
                if self._dfs(p, curr_index + 1, n):
                    return True
            return False
        else:
            return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._dfs(word, 0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class TrieNode(object):
    def __init__(self):
        self.is_term = False
        self.children = {}


class WordDictionaryBFS(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        trie = self.trie
        for c in word:
            if c in trie.children:
                trie = trie.children[c]
            else:
                new_trie_node = TrieNode()
                trie.children[c] = new_trie_node
                trie = new_trie_node

        trie.is_term = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.'
        to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr = [self.trie]

        for c in word:
            next_curr = []
            if c != '.':
                for n in curr:
                    if c in n.children:
                        next_curr.append(n.children[c])
            else:
                for n in curr:
                    next_curr.extend(n.children.values())
            curr = next_curr
            if not curr:
                return False

        return any([n.is_term for n in curr])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
