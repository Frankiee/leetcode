# [Tree-Serialization-Deserialization]
# https://leetcode.com/problems/find-duplicate-subtrees/
# 652. Find Duplicate Subtrees

# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node
# values.
#
# Example 1:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#
#       2
#      /
#     4
# and
#
#     4
# Therefore, you need to return above trees' root in the form of a list.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generate_serialized(self, root, ret, serialized, ret_serialized):
        if not root:
            return "#"

        ser = (
            str(root.val) + ',' +
            self.generate_serialized(root.left, ret, serialized,
                                     ret_serialized) + ',' +
            self.generate_serialized(root.right, ret, serialized,
                                     ret_serialized)
        )

        if ser in serialized and ser not in ret_serialized:
            ret.append(root)
            ret_serialized.add(ser)

        serialized.add(ser)

        return ser

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ret = []
        ret_serialized = set()
        serialized = set()

        self.generate_serialized(root, ret, serialized, ret_serialized)

        return ret
