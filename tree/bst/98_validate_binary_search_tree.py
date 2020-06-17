# [BST]
# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree

# History:
# 1.
# Mar 7, 2020
# 2.
# Apr 22, 2020

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _is_valid_bst(self, root, max_val, min_val):
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        if not self._is_valid_bst(root.left, min(max_val, root.val), min_val):
            return False

        return self._is_valid_bst(root.right, max_val, max(root.val, min_val))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._is_valid_bst(root, float('inf'), float('-inf'))
