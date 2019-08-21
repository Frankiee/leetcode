# [Important]
# https://leetcode.com/problems/short-encoding-of-words/
# 820. Short Encoding of Words

# Given a list of words, we may encode it by writing a reference string S
# and a list of indexes A.
#
# For example, if the list of words is ["time", "me", "bell"], we can write
# it as S = "time#bell#" and indexes = [0, 2, 5].
#
# Then for each index, we will recover the word by reading from the
# reference string from that index until we reach a "#" character.
#
# What is the length of the shortest reference string S possible that
# encodes the given words?
#
# Example:
#
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
#
#
# Note:
#
# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = {}


class Solution(object):
    def __init__(self):
        self.trie = TrieNode()
        self.encoding_len = 0

    def add_to_trie(self, word):
        # return the encoding length delta
        reversed_chars = reversed(list(word))

        additional_length = None
        current_node = self.trie
        for c in reversed_chars:
            if c not in current_node.children:
                trie_node = TrieNode()
                current_node.children[c] = trie_node
            current_node = current_node.children[c]

            if current_node.is_terminal:
                current_node.is_terminal = False
                additional_length = 0
            elif additional_length is not None:
                additional_length += 1

        if not current_node.children:
            current_node.is_terminal = True

        if additional_length is not None:
            return additional_length
        elif current_node.children:
            return 0
        else:
            return len(word) + 1

    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for w in words:
            l = self.add_to_trie(w)
            self.encoding_len += l

        return self.encoding_len
