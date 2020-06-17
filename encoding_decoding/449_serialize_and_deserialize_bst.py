# [Classic, Tree-Serialization-Deserialization]
# https://leetcode.com/problems/serialize-and-deserialize-bst/
# 449. Serialize and Deserialize BST

# History:
# Facebook
# 1.
# Mar 15, 2020
# 2.
# Apr 11, 2020
# 3.
# May 2, 2020

# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection
# link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction
# on how your serialization/deserialization algorithm should work. You just need to ensure that a
# binary search tree can be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and
# deserialize algorithms should be stateless.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec1:
    def _serialize(self, root):
        if not root:
            return ['#']

        ret = [str(root.val)]
        ret.extend(self._serialize(root.left))
        ret.extend(self._serialize(root.right))

        return ret

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ",".join(self._serialize(root))

    def _deserialize(self, chars, curr):
        if chars[curr] == '#':
            return None, curr + 1

        node = TreeNode(int(chars[curr]))
        curr += 1
        node.left, curr = self._deserialize(chars, curr)
        node.right, curr = self._deserialize(chars, curr)

        return node, curr

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node, _ = self._deserialize(data.split(','), 0)

        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec2:
    def _serialize(self, node):
        if not node:
            return ['#']

        ret = [str(node.val)]

        ret.extend(self._serialize(node.left))
        ret.extend(self._serialize(node.right))

        return ret

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ",".join(self._serialize(root))

    def _deserializse(self, token):
        if token[self.curr] == '#':
            self.curr += 1
            return None

        node = TreeNode(int(token[self.curr]))
        self.curr += 1

        node.left = self._deserializse(token)
        node.right = self._deserializse(token)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        token = data.split(',')

        self.curr = 0

        return self._deserializse(token)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
