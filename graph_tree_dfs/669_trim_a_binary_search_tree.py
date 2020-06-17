# https://leetcode.com/problems/trim-a-binary-search-tree/
# 669. Trim a Binary Search Tree

# History:
# Facebook
# 1.
# May 5, 2020

# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so
# that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree,
# so the result should return the new root of the trimmed binary search tree.
#
# Example 1:
# Input:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output:
#     1
#       \
#        2
# Example 2:
# Input:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output:
#       3
#      /
#    2
#   /
#  1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if R >= root.val >= L:
            if root.val > L:
                root.left = self.trimBST(root.left, L, R)
            else:
                root.left = None

            if root.val < R:
                root.right = self.trimBST(root.right, L, R)
            else:
                root.right = None

            return root
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            return self.trimBST(root.right, L, R)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > R:
            return self.trimBST(root.left, L, R)

        if root.val < L:
            return self.trimBST(root.right, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
