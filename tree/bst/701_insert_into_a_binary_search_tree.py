# [BST]
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# 701. Insert into a Binary Search Tree

# History:
# Facebook
# 1.
# Apr 12, 2020

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
# insert the value into the BST. Return the root node of the BST after the insertion. It is
# guaranteed that the new value does not exist in the original BST.
#
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a
# BST after insertion. You can return any of them.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)

        if not root:
            return new_node

        curr = root

        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
            else:
                if not curr.left:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left

        return root
