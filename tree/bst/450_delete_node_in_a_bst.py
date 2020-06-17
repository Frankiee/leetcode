# [BST, Classic]
# https://leetcode.com/problems/delete-node-in-a-bst/
# 450. Delete Node in a BST

# History:
# Facebook
# 1.
# Apr 12, 2020

# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _find_largest_smaller(self, node):
        curr = node.left
        while curr.right:
            curr = curr.right

        return curr

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            if not root.left:
                return root.right

            largest_smaller = self._find_largest_smaller(root)

            largest_smaller.right = root.right

            return root.left
