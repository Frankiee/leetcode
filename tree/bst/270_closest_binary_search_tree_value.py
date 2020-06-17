# [BST]
# https://leetcode.com/problems/closest-binary-search-tree-value/
# 270. Closest Binary Search Tree Value

# History:
# Facebook
# 1.
# Jan 4, 2020
# 2.
# Apr 23, 2020

# Given a non-empty binary search tree and a target value, find the value in the BST that is
# closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4
# Accepted


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return float('inf')

        min_diff = abs(root.val - target)

        if root.val == target:
            return root.val

        if root.val > target:
            min_diff_val = self.closestValue(root.left, target)
        else:
            min_diff_val = self.closestValue(root.right, target)

        if abs(min_diff_val - target) < min_diff:
            return min_diff_val
        else:
            return root.val
