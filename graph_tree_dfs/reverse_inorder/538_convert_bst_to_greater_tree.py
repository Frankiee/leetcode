# [Reverse-Inorder]
# https://leetcode.com/problems/convert-bst-to-greater-tree/
# 538. Convert BST to Greater Tree

# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of
# all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _inorder(self, node, ret):
        if node:
            self._inorder(node.left, ret)
            ret.append(node.val)
            self._inorder(node.right, ret)

    def _reverse_inorder(self, node, values):
        if node:
            self._reverse_inorder(node.right, values)

            node.val += self.total
            self.total += values.pop()

            self._reverse_inorder(node.left, values)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []

        self._inorder(root, values)

        self.total = 0
        self._reverse_inorder(root, values)

        return root
