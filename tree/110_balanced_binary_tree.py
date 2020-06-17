# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree

# History:
# Google
# 1.
# Jun 14, 2020

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more
# than 1.
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _is_balanced(self, node):
        if not node:
            return True, 0

        left_balanced, left_depth = self._is_balanced(node.left)
        if not left_balanced:
            return False, None
        right_balanced, right_depth = self._is_balanced(node.right)
        if not right_balanced:
            return False, None

        if abs(left_depth - right_depth) <= 1:
            return True, max(left_depth, right_depth) + 1

        return False, None

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret, _ = self._is_balanced(root)
        return ret
