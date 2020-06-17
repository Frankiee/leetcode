# https://leetcode.com/problems/implement-trie-prefix-tree/
# 208. Implement Trie (Prefix Tree)

# History:
# Facebook
# 1.
# May 7, 2020

# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.trie_root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.is_terminal = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.trie_root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_terminal

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.trie_root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
