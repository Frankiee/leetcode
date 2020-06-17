# [Tree-Serialization-Deserialization, Classic]
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# 297. Serialize and Deserialize Binary Tree

# https://www.youtube.com/watch?v=JL4OjKV_pGE&t=336s

# History:
# Facebook
# 1.
# Jan 23, 2020
# 2.
# Apr 22, 2020

# Serialization is the process of converting a data structure or object into
# a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is
# no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary tree can be serialized to a
# string and this string can be deserialized to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
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
        tokens = self._serialize(root)

        return ",".join(tokens)

    def _deserialize(self, tokens, idx):
        nxt = tokens[idx]
        idx += 1
        if nxt == '#':
            return None, idx

        root = TreeNode(int(nxt))
        left, idx = self._deserialize(tokens, idx)
        right, idx = self._deserialize(tokens, idx)

        root.left = left
        root.right = right

        return root, idx

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(',')
        node, _ = self._deserialize(tokens, 0)

        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
