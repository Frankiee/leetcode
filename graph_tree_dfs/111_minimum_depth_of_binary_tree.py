# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# Apr 30, 2020

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the
# nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0:
            return right_depth + 1
        if right_depth == 0:
            return left_depth + 1

        return min(left_depth, right_depth) + 1
