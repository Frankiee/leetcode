# https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree

# History:
# Facebook
# 1.
# Mar 27, 2020
# 2.
# Apr 28, 2020
# 3.
# May 15, 2020

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _is_symmetric(self, l, r):
        if not l or not r:
            return l == r

        if l.val != r.val:
            return False

        return self._is_symmetric(l.left, r.right) and self._is_symmetric(l.right, r.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self._is_symmetric(root.left, root.right)
