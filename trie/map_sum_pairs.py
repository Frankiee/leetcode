# https://leetcode.com/problems/map-sum-pairs/description/
# 677. Map Sum Pairs

# Implement a MapSum class with insert, and sum methods.

# For the method insert, you'll be given a pair of (string, integer).
# The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be
# overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix,
# and you need to return the sum of all the pairs' value whose key starts
# with the prefix.

# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5


class TrieNode(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(val=None, children={})

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        current_node = self.root
        for c in key:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                new_node = TrieNode(val=None, children={})
                current_node.children[c] = new_node
                current_node = new_node

        current_node.val = val

    def sum_root(self, node):
        if not node:
            return 0

        s = 0
        if node.val is not None:
            s = s + node.val

        for c in node.children.itervalues():
            s = s + self.sum_root(c)

        return s

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return 0
            current_node = current_node.children[c]

        return self.sum_root(current_node)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
