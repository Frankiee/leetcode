# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# 114. Flatten Binary Tree to Linked List

# History:
# Facebook
# 1.
# Jan 4, 2020
# 2.
# May 6, 2020

# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten_get_sides(self, node):
        if not node:
            return None, None

        if not node.left and not node.right:
            return node, node

        left_left_side, left_right_side = self.flatten_get_sides(node.left)
        right_left_side, right_right_side = self.flatten_get_sides(node.right)

        node.left = None
        if left_left_side:
            node.right = left_left_side
            left_right_side.right = right_left_side
        else:
            node.right = right_left_side

        if right_right_side:
            return node, right_right_side
        else:
            return node, left_right_side

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.flatten_get_sides(root)
