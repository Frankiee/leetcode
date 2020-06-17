# [Archived]
# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree

# History:
# Google
# 1.
# Mar 14, 2020

# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a
# binary tree on a whiteboard so f*** off.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        root.left = right_inverted
        root.right = left_inverted

        return root
