# [Tree-Serialization-Deserialization]
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 106. Construct Binary Tree from Inorder and Postorder Traversal

# History:
# Facebook
# 1.
# Apr 6, 2020

# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _build_tree(self, inorder, postorder, in_l, in_r, post_l, post_r, inorder_idx_map):
        if in_l > in_r:
            return None

        root = postorder[post_r]

        i = inorder_idx_map[root]

        left = self._build_tree(inorder, postorder, in_l, i - 1, post_l, post_l + i - 1 - in_l,
                                inorder_idx_map)
        right = self._build_tree(inorder, postorder, i + 1, in_r, post_l + i - in_l, post_r - 1,
                                 inorder_idx_map)

        return TreeNode(root, left, right)

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        inorder_idx_map = {}
        for i, n in enumerate(inorder):
            inorder_idx_map[n] = i
        return self._build_tree(inorder, postorder, 0, len(inorder) - 1, 0, len(inorder) - 1,
                                inorder_idx_map)
