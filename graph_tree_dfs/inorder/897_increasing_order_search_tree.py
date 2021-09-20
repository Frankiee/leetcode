# https://leetcode.com/problems/increasing-order-search-tree/
# 897. Increasing Order Search Tree

# 1.
# Mar 16, 2019
# 2.
# Sep 18, 2021

# Given a tree, rearrange the tree in in-order so that the leftmost node in
# the tree is now the root of the tree, and every node has no left child and
# only 1 right child.
#
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
# Note:
#
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _inorder(self, node):
        if node:
            left_first, left_last = self._inorder(node.left)
            right_first, right_last = self._inorder(node.right)

            if left_last:
                left_last.right = node

            node.left = None
            node.right = right_first

            return left_first or node, right_last or node

        return None, None

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        first, last = self._inorder(root)

        return first
