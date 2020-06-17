# [Classic]
# https://leetcode.com/problems/stream-of-characters/
# 1032. Stream of Characters

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# May 12, 2020

# Implement the StreamChecker class as follows:
#
# StreamChecker(words): Constructor, init the data structure with the given words.
# query(letter): returns true if and only if for some k >= 1, the last k characters queried (in
# order from oldest to newest, including this letter just queried) spell one of the words in the
# given list.
#
#
# Example:
#
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the wordlist
#
#
# Note:
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.


class Trie(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class StreamCheckerHistory(object):
    def _build_trie(self, word):
        curr_node = self.trie

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Trie()

            curr_node = curr_node.children[c]

        curr_node.is_terminal = True

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        self.s = ""

        self.max_len = 0
        for word in words:
            self._build_trie(word[::-1])
            self.max_len = max(self.max_len, len(word))

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.s = (letter + self.s)[:self.max_len]

        curr_trie = self.trie
        for i in range(len(self.s)):
            if self.s[i] in curr_trie.children:
                curr_trie = curr_trie.children[self.s[i]]
                if curr_trie.is_terminal:
                    return True
            else:
                return False

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class Trie(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class StreamCheckerWaitingList(object):
    def _build_trie(self, word):
        curr_node = self.trie

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Trie()

            curr_node = curr_node.children[c]

        curr_node.is_terminal = True

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        self.wip_nodes = []

        for word in words:
            self._build_trie(word)

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        next_wip_nodes = []

        found = False
        for wip_node in self.wip_nodes:
            if letter in wip_node.children:
                if wip_node.children[letter].is_terminal:
                    found = True
                next_wip_nodes.append(wip_node.children[letter])

        if letter in self.trie.children:
            if self.trie.children[letter].is_terminal:
                found = True
            next_wip_nodes.append(self.trie.children[letter])

        self.wip_nodes = next_wip_nodes

        return found

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
