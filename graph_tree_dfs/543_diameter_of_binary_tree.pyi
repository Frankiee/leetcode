# [Classic, Edge-To-Node-Conversion]
# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# May 15, 2020

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter
# of a binary tree is the length of the longest path between any two nodes in a tree. This path
# may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def _dfs(self, node):
        if not node:
            return 0, 0

        left_ret, left_depth = self._dfs(node.left)
        right_ret, right_depth = self._dfs(node.right)

        depth = max(left_depth + 1, right_depth + 1)
        ret = 1 + left_depth + right_depth

        return max(ret, left_ret, right_ret), depth

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, _ = self._dfs(root)
        return max(0, ret - 1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def _dfs(self, node):
        if not node:
            return 0, -1

        if not node.left and not node.right:
            return 0, 0

        left_ret, left_dist = self._dfs(node.left)
        right_ret, right_dist = self._dfs(node.right)

        return max(
            left_ret,
            right_ret,
            left_dist + right_dist + 2,
        ), max(left_dist, right_dist) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, _ = self._dfs(root)
        return ret
