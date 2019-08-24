# https://leetcode.com/problems/replace-words/
# 648. Replace Words

# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor.
# For example, the root an, followed by other, which can form another word
# another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need
# to replace all the successor in the sentence with the root forming it. If
# a successor has many roots can form it, replace it with the root with the
# shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
# Note:
#
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000


class Node(object):
    def __init__(self):
        self.is_word = False
        self.c = {}


class Solution(object):
    def __init__(self):
        self.trie = Node()

    def _add_to_trie(self, word):
        node = self.trie
        for c in word:
            if c not in node.c:
                new_node = Node()
                node.c[c] = new_node
                node = new_node
            else:
                node = node.c[c]
        node.is_word = True

    def _find_word(self, word):
        node = self.trie
        for i in range(len(word)):
            c = word[i]
            if c not in node.c:
                return word
            else:
                node = node.c[c]
                if node.is_word:
                    return word[0:i + 1]

        return word

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        for word in dict:
            self._add_to_trie(word)

        return " ".join([self._find_word(word) for word in sentence.split()])
