# [Common-Ancestor]
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 236. Lowest Common Ancestor of a Binary Tree

# History:
# Facebook
# 1.
# Mar 15, 2020
# 3.
# Apr 24, 2020

# Related:
# 235. Lowest Common Ancestor of a Binary Search Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given
# nodes in the tree.
#
# According to the definition of LCA on Wikipedia: "The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T that
# has both p and q as descendants (where we allow a node to be a descendant
# of itself)."
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _lowest_common_ancestor(self, root, expected):
        if not root:
            return None, set()

        left_ret, left_contains = self._lowest_common_ancestor(root.left, expected)

        if left_ret:
            return left_ret, left_contains

        if root.val in expected:
            left_contains.add(root.val)
        if left_contains == expected:
            return root, expected

        right_ret, right_contains = self._lowest_common_ancestor(root.right, expected)

        if right_ret:
            return right_ret, right_contains

        left_contains = left_contains | right_contains
        if left_contains == expected:
            return root, expected

        return None, left_contains

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ret, _ = self._lowest_common_ancestor(root, {p.val, q.val})

        return ret
