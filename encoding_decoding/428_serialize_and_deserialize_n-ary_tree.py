# [Tree-Serialization-Deserialization, Classic, Stream]
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
# 428. Serialize and Deserialize N-ary Tree

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# May 12, 2020

# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection
# link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree
# in which each node has no more than N children. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree
# can be serialized to a string and this string can be deserialized to the original tree structure.
#
# For example, you may serialize the following 3-ary tree
#
#
#
# as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow
# this format.
#
# Or you can follow LeetCode's level order traversal serialization format, where each group of
# children is separated by the null value.
#
#
#
# For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,
# 10,null,null,11,null,12,null,13,null,null,14].
#
# You do not necessarily need to follow the above suggested formats, there are many more
# different formats that work so please be creative and come up with different approaches yourself.
#
#
#
# Constraints:
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
# Do not use class member/global/static variables to store states. Your encode and decode
# algorithms should be stateless.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec1:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return '[]'

        ret = []
        ret.append('[')
        ret.append(str(root.val))
        ret.append('[')
        for c in root.children:
            ret.append(self.serialize(c))
        ret.append(']')
        ret.append(']')

        return "".join(ret)

    def _deserialize(self, data):
        self.curr += 1

        if data[self.curr] == ']':
            self.curr += 1
            return None

        num = 0
        while data[self.curr].isdigit():
            num *= 10
            num += int(data[self.curr])

            self.curr += 1

        ret = Node(num, [])

        self.curr += 1

        while data[self.curr] != ']':
            ret.children.append(self._deserialize(data))

        self.curr += 1
        self.curr += 1

        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        self.curr = 0

        return self._deserialize(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec2:
    def _deseralize(self, data, idx):
        idx += 1

        end = idx
        while data[end] not in {'[', ']'}:
            end += 1

        node = Node(data[idx:end], children=[])

        start = end

        while data[start] != ']':
            c, start = self._deseralize(data, start)
            node.children.append(c)

        start += 1

        return node, start

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''

        ret = ['[']
        ret.append(str(root.val))

        for c in root.children:
            ret.append(self.serialize(c))
        ret.append(']')

        return ''.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        tree, _ = self._deseralize(data, 0)

        return tree

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
