# [Tree-Serialization-Deserialization]
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal

# History:
# Google, Facebook
# 1.
# Mar 25, 2020
# 2.
# May 4, 2020

# https://www.youtube.com/watch?v=53aOi0Drp9I&t=323s
# https://github.com/Frankiee/leetcode/blob/master/graph_tree_dfs_recursion/README.md

# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#1262
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionPointer(object):
    def _build_tree(self, preorder, pre_l, pre_r, inorder, in_l, in_r):
        if pre_l > pre_r:
            return None

        root = TreeNode(preorder[pre_l])

        for i in range(in_l, in_r + 1):
            if inorder[i] == preorder[pre_l]:
                break

        left_length = i - in_l
        root.left = self._build_tree(preorder, pre_l + 1, pre_l + left_length, inorder, in_l, i - 1)
        root.right = self._build_tree(preorder, pre_l + left_length + 1, pre_r, inorder, i + 1,
                                      in_r)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self._build_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


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
