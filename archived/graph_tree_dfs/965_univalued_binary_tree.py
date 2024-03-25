# [Archived]
# https://leetcode.com/problems/univalued-binary-tree/
# 965. Univalued Binary Tree

# history
# 1.
# Sep 19, 2021

# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:
#
#
# Input: root = [2,2,2,5,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _is_unival_tree(self, root, val):
        if not root:
            return True

        if root.val != val:
            return False

        return self._is_unival_tree(root.left, val) and self._is_unival_tree(root.right, val)

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self._is_unival_tree(root.left, root.val) and self._is_unival_tree(root.right, root.val)
