# [Common-Ancestor]
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 235. Lowest Common Ancestor of a Binary Search Tree

# History:
# Facebook
# 1.
# Aug 31, 2019
# 2.
# Nov 12, 2019
# 3.
# Apr 30, 2020
# 4.
# May 9, 2020

# Related:
# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: "The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T that
# has both p and q as descendants (where we allow a node to be a descendant
# of itself)."
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionIteration(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        b, s = (p.val, q.val) if p.val >= q.val else (q.val, p.val)

        while root:
            if b >= root.val >= s:
                return root
            elif root.val > b:
                root = root.left
            else:
                root = root.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionRecursion(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        p, q = (p, q) if q.val > p.val else (q, p)

        if p.val <= root.val <= q.val:
            return root

        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)
