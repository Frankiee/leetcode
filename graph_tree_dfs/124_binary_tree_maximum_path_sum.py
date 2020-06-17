# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 124. Binary Tree Maximum Path Sum

# History:
# Facebook
# 1.
# Mar 15, 2020
# 2.
# Apr 13, 2020
# 3.
# May 20, 2020

# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any
# node in the tree along the parent-child connections. The path must contain at least one node
# and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def _dfs(self, node):
        if not node:
            return float('-inf'), float('-inf')

        left_max, left_through_max = self._dfs(node.left)
        right_max, right_through_max = self._dfs(node.right)

        through_max = max(
            left_through_max + node.val,
            node.val,
            right_through_max + node.val,
        )

        curr_max = max(
            left_max,
            right_max,
            through_max,
            left_through_max + node.val + right_through_max,
        )

        return curr_max, through_max

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_max, _ = self._dfs(root)

        return curr_max


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def _dfs(self, node):
        if not node:
            return float('-inf'), float('-inf')

        if not node.left and not node.right:
            return node.val, node.val

        left_ret, left_through = self._dfs(node.left)
        right_ret, right_through = self._dfs(node.right)

        return max(
            left_ret,
            right_ret,
            node.val,
            left_through + node.val,
            right_through + node.val,
            right_through + node.val + left_through
        ), max(
            node.val,
            node.val + left_through,
            node.val + right_through
        )

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, _ = self._dfs(root)

        return ret
