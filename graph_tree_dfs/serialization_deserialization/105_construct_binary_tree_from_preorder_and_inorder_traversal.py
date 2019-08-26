# [Import, Tree-Serialization-Deserialization]
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal

# https://www.youtube.com/watch?v=53aOi0Drp9I&t=323s
# https://github.com/Frankiee/leetcode/blob/master/graph_tree_dfs_recursion/README.md

# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value)

        inorder_root_idx = inorder.index(root_value)

        left_inorder = inorder[:inorder_root_idx]
        right_inorder = inorder[inorder_root_idx + 1:]

        left_preorder = preorder[:len(left_inorder)]
        right_preorder = preorder[len(left_inorder):]

        left_tree = self.buildTree(left_preorder, left_inorder)
        right_tree = self.buildTree(right_preorder, right_inorder)

        root.left = left_tree
        root.right = right_tree

        return root
